from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from shared.config.settings import settings
from shared.tools.audit_logger import log_audit
from shared.tools.file_generator import generate_files
from shared.tools.project_context import get_context
from shared.tools.skill_search import search_skill

from .instructions import build_instruction

root_agent = Agent(
    model=LiteLlm(model=f"openai/{settings.model}"),
    name="tester_agent",
    description="Generates comprehensive test suites adapted to any test framework",
    instruction=build_instruction,
    tools=[search_skill, get_context, generate_files, log_audit],
)
