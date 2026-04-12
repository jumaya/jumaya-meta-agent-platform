import asyncio
import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.runners import InMemoryRunner
from google.genai.types import Content, Part

from shared.config.settings import settings
from shared.tools.audit_logger import log_audit
from shared.tools.project_context import get_context, save_context
from shared.tools.skill_search import search_skill
from architect.instructions import build_instruction

# Configurar env para LiteLlm -> GitHub Models API
os.environ["OPENAI_API_KEY"] = settings.github_token
os.environ["OPENAI_API_BASE"] = "https://models.github.ai/inference"

# Asegurar que el modelo NO tenga doble prefijo
model_name = settings.model
if not model_name.startswith("openai/"):
    model_name = f"openai/{model_name}"

print("=" * 60)
print("TEST: Architect Agent Standalone")
print(f"Model: {model_name}")
print("=" * 60)


async def test():
    # 1. Crear el agente
    agent = Agent(
        model=LiteLlm(model=model_name),
        name="architect_agent",
        description="Analyzes requirements and designs architecture",
        instruction=build_instruction,
        tools=[search_skill, get_context, save_context, log_audit],
    )

    # 2. Crear el runner in-memory
    APP_NAME = "meta_agent_test"
    USER_ID = "test_user"
    SESSION_ID = "test_session_001"

    runner = InMemoryRunner(agent=agent, app_name=APP_NAME)

    # 3. CREAR LA SESION ANTES de ejecutar run_async
    session = await runner.session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
    )
    # Usar el session_id que ADK generó
    actual_session_id = session.id
    print(f"\nSession creada: {actual_session_id}")

    # 4. Enviar el prompt del usuario
    user_message = Content(
        parts=[Part(text=(
            "Diseña la arquitectura para un sistema de gestion de gimnasio. "
            "Es para menos de 100 usuarios, un solo desarrollador, "
            "backend en .NET 9, frontend Angular 18, "
            "base de datos PostgreSQL, deploy en Azure. "
            "Plazo de 3 meses."
        ))]
    )

    print("\n📤 Enviando prompt al Architect Agent...\n")

    # 5. Ejecutar y capturar eventos
    final_response = ""
    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=actual_session_id,
        new_message=user_message,
    ):
        # Capturar respuesta de texto
        if hasattr(event, "content") and event.content:
            for part in event.content.parts:
                if hasattr(part, "text") and part.text:
                    final_response += part.text

        # Debug: mostrar autor del evento
        if hasattr(event, "author"):
            author = event.author if event.author else "system"
            print(f"  📍 Event from: {author}")

        # Debug: mostrar tool calls
        if hasattr(event, "content") and event.content:
            for part in event.content.parts:
                if hasattr(part, "function_call") and part.function_call:
                    fc = part.function_call
                    print(f"  🔧 Tool call: {fc.name}({fc.args})")
                if hasattr(part, "function_response") and part.function_response:
                    fr = part.function_response
                    print(f"  📦 Tool response: {fr.name} -> {str(fr.response)[:200]}...")

    print("\n" + "=" * 60)
    print("📥 RESPUESTA DEL ARCHITECT AGENT:")
    print("=" * 60)
    if final_response:
        # Mostrar max 3000 chars
        print(final_response[:3000])
        if len(final_response) > 3000:
            print(f"\n... ({len(final_response)} chars total)")
    else:
        print("(sin respuesta de texto)")

    # 6. Verificar MongoDB
    from shared.services.persistence.mongodb import get_database
    db = await get_database()

    skill_count = await db.skill_cache.count_documents({})
    print(f"\n📊 Skills en cache MongoDB: {skill_count}")

    audit_count = await db.audit_log.count_documents({})
    print(f"📊 Entries en audit_log: {audit_count}")

    print("\n✅ TEST COMPLETADO")


asyncio.run(test())