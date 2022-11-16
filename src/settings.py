from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_TITLE: str = "Flet-SWAPI"

    SWAPI_URL: str = "https://swapi.dev/api/"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
