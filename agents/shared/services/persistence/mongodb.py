from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from shared.config.settings import settings

_client: AsyncIOMotorClient | None = None


async def get_database() -> AsyncIOMotorDatabase:
    global _client
    if _client is None:
        _client = AsyncIOMotorClient(settings.mongodb_uri)
    return _client[settings.mongodb_database]


async def close_database() -> None:
    global _client
    if _client is not None:
        _client.close()
        _client = None
