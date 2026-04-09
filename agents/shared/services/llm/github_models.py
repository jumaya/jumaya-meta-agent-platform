from __future__ import annotations

import httpx

from shared.config.settings import settings

GITHUB_MODELS_ENDPOINT = "https://models.github.ai/inference/chat/completions"


class GitHubModelsClient:
    """Async client for the GitHub Models API (OpenAI-compatible endpoint)."""

    def __init__(self, model: str | None = None) -> None:
        self._model = model or settings.model

    async def complete(
        self,
        messages: list[dict],
        max_tokens: int = 2000,
        temperature: float = 0.1,
    ) -> str:
        headers = {
            "Authorization": f"Bearer {settings.github_token}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self._model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                GITHUB_MODELS_ENDPOINT,
                headers=headers,
                json=payload,
            )
            response.raise_for_status()

        data = response.json()
        choices = data.get("choices") or []
        if not choices:
            return ""
        return choices[0].get("message", {}).get("content") or ""
