import requests
from fastapi import HTTPException

from app.config import get_settings
from app.logger import get_logger
from app.schemas.coordinates import Coordinates
from app.schemas.location import Location
from app.schemas.weather import Weather

SETTINGS = get_settings()
LOGGER = get_logger()

class SpotifyAPI:
    CLIENT_ID = SETTINGS.spotify_client_id
    CLIENT_SECRET = SETTINGS.spotify_client_secret
    API_BASE_URL = SETTINGS.spotify_api_base_url
    ACCOUNT_BASE_URL = SETTINGS.spotify_account_base_url

    access_token: str

    def authenticate(self):
        LOGGER.info('[SpotifyAPI] Authenticating...')
        response = requests.post(
            url=f'{self.ACCOUNT_BASE_URL}/token',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=dict(grant_type='client_credentials', client_id=self.CLIENT_ID,
                      client_secret=self.CLIENT_SECRET))

        if not response.ok:
            raise HTTPException(
                status_code=response.status_code, detail=response.reason)
        self.access_token = response.json().get('access_token')

    def get_playlists_by_category(self, category_id: str):
        LOGGER.info(f'[SpotifyAPI] Getting {category_id} playlists...')
        url = f'{self.API_BASE_URL}/browse/categories/{category_id}/playlists'
        headers = dict(authorization=f'Bearer {self.access_token}')
        response = requests.get(url=url, headers=headers)
        if not response.ok:
            raise HTTPException(
                status_code=response.status_code, detail=response.reason)
        return response.json()

