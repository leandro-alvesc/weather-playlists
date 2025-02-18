from pydantic import BaseModel

from .weather import Weather
from .playlists import Playlist


class FavoriteInput(BaseModel):
    weather: Weather
    playlist: Playlist


class FavoriteOutput(BaseModel):
    id: str
    weather: Weather
    playlist: Playlist
