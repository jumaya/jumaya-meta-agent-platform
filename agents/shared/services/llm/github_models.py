import httpx

from shared.config.settings import settings


class GitHubModelsClient:
    BASE_URL = "https://models.github.ai/inference/chat/completions"

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
        async with httpx.AsyncClient(timeout=120.0) as client:
            try:
                response = await client.post(self.BASE_URL, headers=headers, json=payload)
                response.raise_for_status()
            except httpx.HTTPStatusError as exc:
                raise RuntimeError(
                    f"GitHub Models API request failed [{exc.response.status_code}]: "
                    f"{exc.response.text}"
                ) from exc
        data = response.json()
        return data["choices"][0]["message"]["content"]
