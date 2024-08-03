from firedantic import Model

from app.schemas.favorite import FavoriteOutput
from app.schemas.weather import Weather
from app.schemas.playlists import Playlist


class Favorite(Model):
    __collection__ = "favorites"
    user_id: str
    weather: Weather
    playlist: Playlist

    def to_schema(self):
        return FavoriteOutput(_id=self.id, user_id=self.user_id,
                              weather=self.weather, playlist=self.playlist)
        
