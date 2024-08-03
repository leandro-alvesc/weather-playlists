from pydantic import BaseModel
from typing import Optional, List

from .coordinates import Coordinates
from .location import Location
from .weather import Weather


class Playlist(BaseModel):
    name: str
    description: str
    category: str
    owner: str
    url: str
    image_url: str


class Playlists(BaseModel):
    coordinates: Coordinates
    location: Location
    weather: Weather
    playlists: Optional[List[Playlist]]
    
