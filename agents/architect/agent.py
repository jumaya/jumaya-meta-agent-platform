import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from shared.tools.audit_logger import log_audit
from shared.tools.project_context import get_context, save_context
from shared.tools.skill_search import search_skill

from .instructions import build_instruction

DEFAULT_MODEL = os.getenv("ARCHITECT_MODEL", "anthropic/claude-sonnet-4-20250514")

root_agent = Agent(
    model=LiteLlm(model=DEFAULT_MODEL),
    name="architect_agent",
    description="Analyzes requirements and designs architecture through a lean interview process",
    instruction=build_instruction,
    tools=[search_skill, get_context, save_context, log_audit],
)
