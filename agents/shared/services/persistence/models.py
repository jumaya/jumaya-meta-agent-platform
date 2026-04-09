from datetime import datetime, timezone
from enum import Enum

from pydantic import BaseModel, Field


class ProjectType(str, Enum):
    NEW_APP = "NEW_APP"
    MIGRATION = "MIGRATION"
    MODERNIZATION = "MODERNIZATION"
    EXTENSION = "EXTENSION"


class SessionStatus(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    ERROR = "ERROR"


class SourcePriority(str, Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"


class BackendStack(BaseModel):
    language: str = ""
    framework: str = ""
    version: str = ""


class FrontendStack(BaseModel):
    framework: str = ""
    version: str = ""
    styling: str = ""


class ProjectStack(BaseModel):
    backend: BackendStack = Field(default_factory=BackendStack)
    frontend: FrontendStack = Field(default_factory=FrontendStack)


class ProjectArchitecture(BaseModel):
    pattern: str = ""
    backend_pattern: str = ""
    frontend_pattern: str = ""


class ProjectSecurity(BaseModel):
    auth_strategy: str = ""
    auth_provider: str = ""
    rbac: bool = False
    compliance: list[str] = Field(default_factory=list)
    multi_tenant: bool = False


class ProjectContext(BaseModel):
    name: str
    description: str = ""
    type: ProjectType = ProjectType.NEW_APP
    stack: ProjectStack = Field(default_factory=ProjectStack)
    architecture: ProjectArchitecture = Field(default_factory=ProjectArchitecture)
    security: ProjectSecurity = Field(default_factory=ProjectSecurity)
    decisions: list[dict] = Field(default_factory=list)
    model_used: str = ""  # Tracks which model was used (for audit purposes)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class SkillCache(BaseModel):
    query: str
    stack_tags: list[str] = Field(default_factory=list)
    content: str
    content_embedding: list[float] = Field(default_factory=list)
    source_urls: list[str] = Field(default_factory=list)
    token_count: int = 0
    fetched_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    ttl_days: int = 30
    expires_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class StepRecord(BaseModel):
    agent: str
    output_summary: str
    tokens_used: int = 0


class Session(BaseModel):
    project_id: str
    pipeline: str
    current_step: int = 0
    steps_completed: list[StepRecord] = Field(default_factory=list)
    total_tokens_used: int = 0
    status: SessionStatus = SessionStatus.IN_PROGRESS


class SourceWhitelist(BaseModel):
    domain: str
    priority: SourcePriority = SourcePriority.MEDIUM
    trust_score: float = 0.85
    categories: list[str] = Field(default_factory=list)
    active: bool = True


class AuditEntry(BaseModel):
    session_id: str
    project_id: str
    agent: str
    action: str
    input_tokens: int = 0
    output_tokens: int = 0
    model: str
    duration_ms: int = 0
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
