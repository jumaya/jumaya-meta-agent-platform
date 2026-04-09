from shared.config.settings import settings
from shared.services.llm.github_models import GitHubModelsClient


class SkillExtractor:
    SYSTEM_PROMPT = (
        "You are a technical knowledge extractor. "
        "Given raw web content about a software development topic, "
        "extract the most relevant patterns, rules, best practices, and code examples. "
        "Be concise. Output structured markdown. Max 2000 tokens."
    )

    def __init__(self, model: str | None = None) -> None:
        self._client = GitHubModelsClient(model=model or settings.model)

    async def extract(self, content: str, query: str, max_tokens: int = 2000) -> str:
        truncated = content[: settings.skill_max_tokens * 4]

        messages = [
            {"role": "system", "content": self.SYSTEM_PROMPT},
            {
                "role": "user",
                "content": (
                    f"Topic: {query}\n\n"
                    f"Raw content:\n{truncated}\n\n"
                    "Extract the key patterns, rules, and examples."
                ),
            },
        ]

        return await self._client.complete(messages=messages, max_tokens=max_tokens)
