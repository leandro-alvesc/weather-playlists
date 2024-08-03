from typing import List, Self

from app.models.base_firestore_model import FirestoreBaseModel
from app.schemas.favorite import FavoriteOutput
from app.schemas.weather import Weather
from app.schemas.playlists import Playlist


class Favorite(FirestoreBaseModel):
    __collection__ = "favorites"
    user_id: str
    weather: Weather
    playlist: Playlist

    @classmethod
    def list_favorites(cls, user_id: str) -> List[Self]:
        return cls.find(dict(user_id=user_id))

    def to_schema(self):
        return FavoriteOutput(id=self.id, weather=self.weather,
                              playlist=self.playlist)
        
