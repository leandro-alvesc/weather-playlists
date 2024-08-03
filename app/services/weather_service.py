import requests

from app.main import get_settings
from app.schemas.coordinates import Coordinates

SETTINGS = get_settings()

class WeatherService:
    BASE_URL = SETTINGS.open_weather_api_base_url
    @staticmethod
    def get_coordinates(city_code: str, state_code: str,
                        country_code: str) -> Coordinates:
        pass

    @classmethod
    def make_request(cls, path: str, params: dict = None) -> dict:
        response = requests.get(f'{cls.BASE_URL}/{path}', params=params)
        if response.ok:
            return response.json()
