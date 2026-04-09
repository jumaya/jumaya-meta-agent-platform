from shared.services.persistence.models import AuditEntry
from shared.services.persistence.mongodb import get_database


async def log_audit(
    agent: str,
    action: str,
    tokens_in: int,
    tokens_out: int,
    model: str,
    session_id: str = "",
    project_id: str = "",
    duration_ms: int = 0,
) -> None:
    """Log an audit entry for agent actions.

    Args:
        agent: Name of the agent performing the action.
        action: Description of the action performed.
        tokens_in: Number of input tokens consumed.
        tokens_out: Number of output tokens produced.
        model: LLM model used.
        session_id: Optional session identifier.
        project_id: Optional project identifier.
        duration_ms: Action duration in milliseconds.
    """
    db = await get_database()
    entry = AuditEntry(
        session_id=session_id,
        project_id=project_id,
        agent=agent,
        action=action,
        input_tokens=tokens_in,
        output_tokens=tokens_out,
        model=model,
        duration_ms=duration_ms,
    )
    await db["audit_log"].insert_one(entry.model_dump())
