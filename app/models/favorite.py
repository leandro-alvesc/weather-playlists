from firedantic import Model

from app.schemas.weather import Weather
from app.schemas.playlists import Playlist


class Favorite(Model):
    __collection__ = "favorites"
    weather: Weather
    playlist: Playlist
