import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # MongoDB
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_database: str = "meta_agent"

    # GitHub Models API
    github_token: str = ""
    model: str = "gpt-4o"

    # Skill Resolution
    skill_cache_ttl_days: int = 30
    skill_max_tokens: int = 2000

    # Misc
    log_level: str = "INFO"


settings = Settings()

# Configure LiteLLM to use GitHub Models API (OpenAI-compatible endpoint)
if settings.github_token:
    os.environ.setdefault("OPENAI_API_KEY", settings.github_token)
    os.environ.setdefault("OPENAI_API_BASE", "https://models.github.ai/inference")
