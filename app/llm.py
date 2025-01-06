from crewai import LLM

from app.config import settings

llm = LLM(model=settings.AZURE_MODEL_NAME, api_key=settings.AZURE_API_KEY, api_base=settings.AZURE_ENDPOINT,
    api_version=settings.AZURE_API_VERSION )
