from shared.services.context.project_context import ProjectContextService

_service = ProjectContextService()


async def get_context(project_id: str) -> dict:
    """Retrieve the full project context from MongoDB.

    Args:
        project_id: The MongoDB ObjectId string or project name.

    Returns:
        Project context as a dictionary, or a message if not found.
    """
    ctx = await _service.get(project_id)
    if ctx:
        return ctx.model_dump()
    return {"message": f"No project found with id/name '{project_id}'. Use save_context to create one."}


async def save_context(project_id: str, data: dict) -> str:
    """Create or update project context in MongoDB.

    Args:
        project_id: The project name or MongoDB ObjectId.
        data: Dictionary of fields to save.

    Returns:
        Confirmation message.
    """
    # Intentar actualizar primero
    updated = await _service.update(project_id, data)
    if updated:
        return f"Project '{project_id}' updated successfully."

    # Si no existe, crear nuevo
    from shared.services.persistence.models import ProjectContext
    new_context = ProjectContext(name=project_id, **{k: v for k, v in data.items() if k != "name"})
    new_id = await _service.create(new_context)
    return f"Project '{project_id}' created with id: {new_id}"