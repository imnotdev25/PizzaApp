from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )

    # Database
    POSTGRES_URI: str = "postgresql+asyncpg://postgres:postgres@db:5432/postgres"

    # Azure AI
    AZURE_ENDPOINT: str = "https://api.openai.com"
    AZURE_API_KEY: str = "api-key"
    AZURE_API_VERSION: str = "2021-09-01"
    AZURE_MODEL_NAME: str = "azure/gpt-4o"


settings = Settings()