from datetime import datetime, timezone

from bson import ObjectId
from bson.errors import InvalidId

from shared.services.persistence.models import ProjectContext
from shared.services.persistence.mongodb import get_database


class ProjectContextService:
    COLLECTION = "project_contexts"

    async def create(self, context: ProjectContext) -> str:
        db = await get_database()
        result = await db[self.COLLECTION].insert_one(context.model_dump())
        return str(result.inserted_id)

    async def get(self, project_id: str) -> ProjectContext | None:
        db = await get_database()
        # Intentar buscar por ObjectId primero
        try:
            doc = await db[self.COLLECTION].find_one({"_id": ObjectId(project_id)})
        except (InvalidId, Exception):
            # Si no es un ObjectId válido, buscar por nombre
            doc = await db[self.COLLECTION].find_one({"name": project_id})
        if doc:
            doc.pop("_id", None)
            return ProjectContext(**doc)
        return None

    async def update(self, project_id: str, updates: dict) -> bool:
        db = await get_database()
        updates["updated_at"] = datetime.now(timezone.utc)
        # Intentar por ObjectId, si falla por nombre
        try:
            query = {"_id": ObjectId(project_id)}
        except (InvalidId, Exception):
            query = {"name": project_id}
        result = await db[self.COLLECTION].update_one(query, {"$set": updates})
        return result.modified_count > 0

    async def delete(self, project_id: str) -> bool:
        db = await get_database()
        try:
            query = {"_id": ObjectId(project_id)}
        except (InvalidId, Exception):
            query = {"name": project_id}
        result = await db[self.COLLECTION].delete_one(query)
        return result.deleted_count > 0

    async def list_all(self) -> list[ProjectContext]:
        db = await get_database()
        cursor = db[self.COLLECTION].find({})
        contexts = []
        async for doc in cursor:
            doc.pop("_id", None)
            contexts.append(ProjectContext(**doc))
        return contexts