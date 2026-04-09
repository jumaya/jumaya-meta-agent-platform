from shared.services.skill_resolution.cache import SkillCacheManager
from shared.services.skill_resolution.extractor import SkillExtractor
from shared.services.skill_resolution.web_search import BingSearchProvider
from shared.services.persistence.models import SkillCache


class SkillResolutionEngine:
    def __init__(self, extractor_model: str = "openai/gpt-4o-mini") -> None:
        self._cache = SkillCacheManager()
        self._search = BingSearchProvider()
        self._extractor = SkillExtractor(model=extractor_model)

    async def resolve(self, query: str, stack_tags: list[str]) -> str:
        cached = await self._cache.lookup(query, stack_tags)
        if cached:
            return cached.content

        search_results = await self._search.search(query, stack_tags)
        if not search_results:
            return f"No skill information found for: {query}"

        combined_content = ""
        source_urls: list[str] = []
        for result in search_results[:3]:
            try:
                page_content = await self._search.fetch_content(result["url"])
                combined_content += f"\n\n## Source: {result['url']}\n{page_content[:3000]}"
                source_urls.append(result["url"])
            except Exception:
                combined_content += f"\n\n## Snippet from {result['url']}\n{result['snippet']}"
                source_urls.append(result["url"])

        extracted = await self._extractor.extract(combined_content, query)
        token_count = len(extracted.split()) * 4 // 3

        await self._cache.save(
            query=query,
            stack_tags=stack_tags,
            content=extracted,
            source_urls=source_urls,
            token_count=token_count,
        )

        return extracted
