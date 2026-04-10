import asyncio
from shared.services.skill_resolution.engine import SkillResolutionEngine

async def test():
    engine = SkillResolutionEngine()

    print("=== Skill Resolution Engine - Full Pipeline ===\n")
    print("1. Buscando en internet...")
    print("2. Descargando contenido...")
    print("3. Extrayendo con LLM...")
    print("4. Cacheando en MongoDB...\n")

    skill = await engine.resolve(
        query="Clean Architecture best practices",
        stack_tags=["dotnet", "csharp"],
    )

    print(f"Skill extraído ({len(skill)} chars):\n")
    print(skill[:1000])
    print("\n=== DONE ===")

asyncio.run(test())