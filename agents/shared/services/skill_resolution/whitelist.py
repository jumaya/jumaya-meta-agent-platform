from shared.services.persistence.models import SourcePriority, SourceWhitelist
from shared.services.persistence.mongodb import get_database
from shared.config.whitelist_seed import DEFAULT_SOURCES


class SourceWhitelistManager:
    COLLECTION = "source_whitelist"

    async def get_active_domains(self) -> list[str]:
        db = await get_database()
        cursor = db[self.COLLECTION].find({"active": True}, {"domain": 1})
        return [doc["domain"] async for doc in cursor]

    async def get_by_priority(self, priority: SourcePriority) -> list[SourceWhitelist]:
        db = await get_database()
        cursor = db[self.COLLECTION].find({"priority": priority.value, "active": True})
        return [SourceWhitelist(**doc) async for doc in cursor]

    async def seed_defaults(self) -> int:
        db = await get_database()
        count = await db[self.COLLECTION].count_documents({})
        if count > 0:
            return 0
        result = await db[self.COLLECTION].insert_many(DEFAULT_SOURCES)
        return len(result.inserted_ids)

    async def add_source(self, source: SourceWhitelist) -> str:
        db = await get_database()
        result = await db[self.COLLECTION].insert_one(source.model_dump())
        return str(result.inserted_id)

    async def deactivate(self, domain: str) -> bool:
        db = await get_database()
        result = await db[self.COLLECTION].update_one(
            {"domain": domain}, {"$set": {"active": False}}
        )
        return result.modified_count > 0
