from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = 'Weather Playlists'
    developer_email: str = ''
    open_weather_api_key: str = ''
    open_weather_api_base_url: str = ''

    model_config = SettingsConfigDict(env_file=".env")
