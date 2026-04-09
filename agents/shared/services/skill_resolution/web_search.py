import httpx

from shared.config.settings import settings
from shared.services.skill_resolution.whitelist import SourceWhitelistManager


class BingSearchProvider:
    def __init__(self) -> None:
        self._whitelist = SourceWhitelistManager()

    async def search(self, query: str, stack_tags: list[str], max_results: int = 5) -> list[dict]:
        domains = await self._whitelist.get_active_domains()
        if not domains:
            return []

        site_filter = " OR ".join(f"site:{d}" for d in domains[:10])
        tag_str = " ".join(stack_tags[:3]) if stack_tags else ""
        full_query = f"{query} {tag_str} ({site_filter})".strip()

        headers = {"Ocp-Apim-Subscription-Key": settings.bing_search_key}
        params = {"q": full_query, "count": max_results, "mkt": "en-US"}

        async with httpx.AsyncClient(timeout=15.0) as client:
            response = await client.get(
                settings.bing_search_endpoint, headers=headers, params=params
            )
            response.raise_for_status()

        data = response.json()
        results = []
        for item in data.get("webPages", {}).get("value", []):
            results.append(
                {
                    "url": item.get("url", ""),
                    "title": item.get("name", ""),
                    "snippet": item.get("snippet", ""),
                }
            )
        return results

    async def fetch_content(self, url: str) -> str:
        import html2text

        async with httpx.AsyncClient(timeout=20.0, follow_redirects=True) as client:
            response = await client.get(url, headers={"User-Agent": "MetaAgent/1.0"})
            response.raise_for_status()

        converter = html2text.HTML2Text()
        converter.ignore_links = True
        converter.ignore_images = True
        return converter.handle(response.text)
