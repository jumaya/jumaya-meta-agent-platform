from bson import ObjectId

from shared.services.persistence.models import Session, SessionStatus, StepRecord
from shared.services.persistence.mongodb import get_database


class SessionManager:
    COLLECTION = "sessions"

    async def create(self, project_id: str, pipeline: str) -> str:
        db = await get_database()
        session = Session(project_id=project_id, pipeline=pipeline)
        result = await db[self.COLLECTION].insert_one(session.model_dump())
        return str(result.inserted_id)

    async def get(self, session_id: str) -> Session | None:
        db = await get_database()
        doc = await db[self.COLLECTION].find_one({"_id": ObjectId(session_id)})
        if doc:
            doc.pop("_id", None)
            return Session(**doc)
        return None

    async def record_step(self, session_id: str, step: StepRecord) -> None:
        db = await get_database()
        await db[self.COLLECTION].update_one(
            {"_id": ObjectId(session_id)},
            {
                "$push": {"steps_completed": step.model_dump()},
                "$inc": {
                    "current_step": 1,
                    "total_tokens_used": step.tokens_used,
                },
            },
        )

    async def complete(self, session_id: str) -> None:
        db = await get_database()
        await db[self.COLLECTION].update_one(
            {"_id": ObjectId(session_id)},
            {"$set": {"status": SessionStatus.COMPLETED.value}},
        )

    async def fail(self, session_id: str, error: str) -> None:
        db = await get_database()
        await db[self.COLLECTION].update_one(
            {"_id": ObjectId(session_id)},
            {"$set": {"status": SessionStatus.ERROR.value, "error": error}},
        )
