import httpx
from duckduckgo_search import AsyncDDGS

from shared.services.skill_resolution.whitelist import SourceWhitelistManager


class DuckDuckGoSearchProvider:
    def __init__(self) -> None:
        self._whitelist = SourceWhitelistManager()

    async def search(self, query: str, stack_tags: list[str], max_results: int = 5) -> list[dict]:
        tag_str = " ".join(stack_tags[:3]) if stack_tags else ""
        domains = await self._whitelist.get_active_domains()
        site_filter = " OR ".join(f"site:{d}" for d in domains[:10]) if domains else ""
        if site_filter:
            full_query = f"{query} {tag_str} ({site_filter})".strip()
        else:
            full_query = f"{query} {tag_str}".strip()

        results = []
        async with AsyncDDGS() as ddgs:
            async for r in ddgs.text(full_query, max_results=max_results):
                results.append({
                    "url": r.get("href", ""),
                    "title": r.get("title", ""),
                    "snippet": r.get("body", ""),
                })
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
