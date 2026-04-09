import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from shared.config.settings import settings
from shared.tools.audit_logger import log_audit
from shared.tools.project_context import get_context
from shared.tools.skill_search import search_skill

from .instructions import build_instruction

os.environ["OPENAI_API_KEY"] = settings.github_token
os.environ["OPENAI_API_BASE"] = "https://models.github.ai/inference"

root_agent = Agent(
    model=LiteLlm(model=f"openai/{settings.model}"),
    name="security_agent",
    description="Reviews code for OWASP vulnerabilities and security best practices",
    instruction=build_instruction,
    tools=[search_skill, get_context, log_audit],
)
