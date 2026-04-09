from shared.services.context.project_context import ProjectContextService

_service = ProjectContextService()


async def get_context(project_id: str) -> dict:
    """Retrieve the full project context from MongoDB.

    Args:
        project_id: The MongoDB ObjectId string of the project.

    Returns:
        Project context as a dictionary, or empty dict if not found.
    """
    ctx = await _service.get(project_id)
    return ctx.model_dump() if ctx else {}


async def save_context(project_id: str, data: dict) -> bool:
    """Update project context fields in MongoDB.

    Args:
        project_id: The MongoDB ObjectId string of the project.
        data: Dictionary of fields to update.

    Returns:
        True if the update was successful.
    """
    return await _service.update(project_id, data)
