from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # GitHub Models API
    github_token: str = ""
    model: str = "claude-sonnet-4.6"

    # MongoDB
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_database: str = "meta_agent"

    # Skill Resolution
    skill_cache_ttl_days: int = 30
    skill_max_tokens: int = 2000

    # General
    log_level: str = "INFO"


settings = Settings()
