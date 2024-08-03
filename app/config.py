from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Weather Playlists'
    developer_email: str = ''
    open_weather_api_key: str = ''
    open_weather_api_base_url: str = ''
    spotify_client_id: str = ''
    spotify_client_secret: str = ''
    spotify_account_base_url: str = ''
    spotify_api_base_url: str = ''

    model_config = SettingsConfigDict(env_file=".env")


@lru_cache
def get_settings():
    return Settings()
