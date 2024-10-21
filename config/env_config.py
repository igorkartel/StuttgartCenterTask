from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvConfig(BaseSettings):
    # Django
    SECRET_KEY: str
    # Database_PostgreSQL
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_DATABASE: str
    DB_ENGINE: str
    # Redis
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_CONNECTION: str

    model_config = SettingsConfigDict(env_file=".env")


env_config = EnvConfig()
