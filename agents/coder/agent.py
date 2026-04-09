import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from shared.tools.audit_logger import log_audit
from shared.tools.file_generator import generate_files
from shared.tools.project_context import get_context
from shared.tools.skill_search import search_skill

from .instructions import build_instruction

DEFAULT_MODEL = os.getenv("CODER_MODEL", "anthropic/claude-sonnet-4-20250514")

root_agent = Agent(
    model=LiteLlm(model=DEFAULT_MODEL),
    name="coder_agent",
    description="Generates production-ready code for any language and framework",
    instruction=build_instruction,
    tools=[search_skill, get_context, generate_files, log_audit],
)
