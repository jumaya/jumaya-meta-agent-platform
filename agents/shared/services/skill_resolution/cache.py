from datetime import datetime, timedelta, timezone

from shared.config.settings import settings
from shared.services.persistence.models import SkillCache
from shared.services.persistence.mongodb import get_database


class SkillCacheManager:
    COLLECTION = "skill_cache"

    async def lookup(self, query: str, stack_tags: list[str]) -> SkillCache | None:
        db = await get_database()
        now = datetime.now(timezone.utc)
        doc = await db[self.COLLECTION].find_one(
            {
                "query": query,
                "stack_tags": {"$all": stack_tags},
                "expires_at": {"$gt": now},
            }
        )
        if doc:
            doc.pop("_id", None)
            return SkillCache(**doc)
        return None

    async def save(
        self,
        query: str,
        stack_tags: list[str],
        content: str,
        source_urls: list[str],
        token_count: int,
        embedding: list[float] | None = None,
    ) -> None:
        db = await get_database()
        now = datetime.now(timezone.utc)
        entry = SkillCache(
            query=query,
            stack_tags=stack_tags,
            content=content,
            content_embedding=embedding or [],
            source_urls=source_urls,
            token_count=token_count,
            fetched_at=now,
            ttl_days=settings.skill_cache_ttl_days,
            expires_at=now + timedelta(days=settings.skill_cache_ttl_days),
        )
        await db[self.COLLECTION].replace_one(
            {"query": query, "stack_tags": {"$all": stack_tags}},
            entry.model_dump(),
            upsert=True,
        )

    async def invalidate_expired(self) -> int:
        db = await get_database()
        result = await db[self.COLLECTION].delete_many(
            {"expires_at": {"$lte": datetime.now(timezone.utc)}}
        )
        return result.deleted_count
