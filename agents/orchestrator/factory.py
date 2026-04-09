from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from shared.config.settings import settings


class DynamicAgentFactory:
    """Creates agents with dynamic instruction composition. All agents use settings.model."""

    def create_agent(
        self,
        name: str,
        instruction: str,
        tools: list,
    ) -> Agent:
        return Agent(
            model=LiteLlm(model=f"openai/{settings.model}"),
            name=name,
            instruction=instruction,
            tools=tools,
        )
