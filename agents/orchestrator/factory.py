from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

from shared.config.model_presets import MODEL_PRESETS


class DynamicAgentFactory:
    """Creates agents with user-chosen model and dynamic instructions."""

    def create_agent(
        self,
        name: str,
        role: str,
        instruction: str,
        tools: list,
        preset: str = "auto",
        custom_model: str | None = None,
    ) -> Agent:
        model_str = custom_model or self._resolve_model(role, preset)
        model = LiteLlm(model=model_str) if "/" in model_str else model_str

        return Agent(
            model=model,
            name=name,
            instruction=instruction,
            tools=tools,
        )

    def _resolve_model(self, role: str, preset: str) -> str:
        preset_config = MODEL_PRESETS.get(preset, MODEL_PRESETS["auto"])
        assignments = preset_config.get("assignments", {})
        return assignments.get(role, "gemini-2.5-flash")
