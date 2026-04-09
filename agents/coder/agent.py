import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from shared.config.settings import settings
from shared.tools.audit_logger import log_audit
from shared.tools.file_generator import generate_files
from shared.tools.project_context import get_context
from shared.tools.skill_search import search_skill

from .instructions import build_instruction

os.environ.setdefault("OPENAI_API_KEY", settings.github_token)
os.environ.setdefault("OPENAI_API_BASE", "https://models.github.ai/inference")

root_agent = Agent(
    model=LiteLlm(model=f"openai/{settings.model}"),
    name="coder_agent",
    description="Generates production-ready code for any language and framework",
    instruction=build_instruction,
    tools=[search_skill, get_context, generate_files, log_audit],
)
