import os

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from shared.config.settings import settings


class DynamicAgentFactory:
    """Creates agents with dynamic instructions. All agents use the global model from settings."""

    def create_agent(
        self,
        name: str,
        instruction: str,
        tools: list,
    ) -> Agent:
        os.environ.setdefault("OPENAI_API_KEY", settings.github_token)
        os.environ.setdefault("OPENAI_API_BASE", "https://models.github.ai/inference")

        return Agent(
            model=LiteLlm(model=f"openai/{settings.model}"),
            name=name,
            instruction=instruction,
            tools=tools,
        )
