from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "CoachMe API"
    app_version: str = "0.1.0"
    bebug: bool = True

    class Config:
        env_file = "development"

settings = Settings()