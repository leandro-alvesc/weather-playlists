import requests
from fastapi import HTTPException

from app.config import get_settings
from app.logger import get_logger
from app.schemas.coordinates import Coordinates
from app.schemas.location import Location
from app.schemas.weather import Weather

SETTINGS = get_settings()
LOGGER = get_logger()

class OpenWeatherAPI:
    BASE_URL: str = SETTINGS.open_weather_api_base_url
    API_KEY: str = SETTINGS.open_weather_api_key
    GEOCODING_PATH: str = '/geo/1.0/direct'
    CURRENT_WEATHER_PATH: str = '/data/2.5/weather'

    @classmethod
    def get_weather(cls, coordinates: Coordinates) -> Weather:
        params = dict(lat=coordinates.latitude, lon=coordinates.longitude,
                      units='metric')
        data = cls.make_request(cls.CURRENT_WEATHER_PATH, params)
        weather = data.get('weather') and data.get('weather')[0]

        return weather and Weather(
            city=data.get('name'),
            name=weather.get('main'),
            description=weather.get('description'),
            temperature=data.get('main').get('temp'),
            feels_like=data.get('main').get('feels_like'),
            humidity=data.get('main').get('humidity'))

    @classmethod
    def get_coordinates(cls, location: Location) -> Coordinates:
        query = f'{location.city_name},{location.state_code},' \
                f'{location.country_code}'
        data = cls.make_request(cls.GEOCODING_PATH, dict(q=query))
        location = data[0] if len(data) else None

        return location and Coordinates(
            name=location.get('name'),
            state=location.get('state'),
            country=location.get('country'),
            latitude='{:0.2f}'.format(location.get('lat')),
            longitude='{:0.2f}'.format(location.get('lon'))
        )


    @classmethod
    def make_request(cls, path: str, params: dict = dict()) -> dict:
        params['appid'] = cls.API_KEY

        LOGGER.info(f'[OpenWeatherApi] - Getting path: {path}')
        LOGGER.info(f'[OpenWeatherApi] - Params: {params}')

        response = requests.get(f'{cls.BASE_URL}{path}', params=params)
        if response.ok:
            return response.json()

        raise HTTPException(
            status_code=response.status_code, detail=response.reason)
