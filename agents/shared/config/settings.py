from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # MongoDB
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_database: str = "meta_agent"

    # API Keys
    google_api_key: str = ""
    openai_api_key: str = ""
    anthropic_api_key: str = ""
    bing_search_key: str = ""

    # Skill Resolution
    skill_cache_ttl_days: int = 30
    skill_max_tokens: int = 2000
    bing_search_endpoint: str = "https://api.bing.microsoft.com/v7.0/search"

    # Agent defaults
    default_model_preset: str = "auto"
    log_level: str = "INFO"


settings = Settings()
