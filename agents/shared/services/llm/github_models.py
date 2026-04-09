import httpx

from shared.config.settings import settings


class GitHubModelsClient:
    """Async client for the GitHub Models API (OpenAI-compatible)."""

    BASE_URL = "https://models.github.ai/inference"

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
            "model": settings.model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
        }
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.BASE_URL}/chat/completions",
                headers=headers,
                json=payload,
            )
            response.raise_for_status()

        data = response.json()
        try:
            return data["choices"][0]["message"]["content"] or ""
        except (KeyError, IndexError) as exc:
            raise ValueError(f"Unexpected response structure from GitHub Models API: {data}") from exc
