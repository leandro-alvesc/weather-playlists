from fastapi import HTTPException
from typing import List

from app.integrations.open_weather_api import OpenWeatherAPI
from app.integrations.spotify_api import SpotifyAPI
from app.models.favorite import Favorite
from app.models.user import User
from app.schemas.favorite import FavoriteInput
from app.schemas.location import Location
from app.schemas.playlists import Playlists, Playlist


class PlaylistService:
    open_weather_api: OpenWeatherAPI = OpenWeatherAPI()
    spotify_api: SpotifyAPI = SpotifyAPI()

    @classmethod
    def get_playlist_by_location(cls, location: Location) -> Playlists:
        coordinates = cls.open_weather_api.get_coordinates(location)
        weather = cls.open_weather_api.get_weather(coordinates)
        cls.spotify_api.authenticate()

        category_id = 'classical'
        if weather.temperature > 25:
            category_id = 'pop'
        elif weather.temperature >= 10:
            category_id = 'rock'

        response = cls.spotify_api.get_playlists_by_category(category_id)
        playlists = response.get('playlists').get('items')

        return Playlists(
            coordinates=coordinates,
            location=location,
            weather=weather,
            playlists=[
                Playlist(
                    name=p.get('name'),
                    description=p.get('description'),
                    category=response.get('message'),
                    owner=p.get('owner').get('display_name'),
                    url=p.get('external_urls').get('spotify'),
                    image_url=p.get('images')[0].get('url') if p.get(
                        'images') else None
                ) for p in playlists]
        )

    @staticmethod
    def list_favorites(user_email: str) -> List[Favorite]:
        user = User.get_user_by_email(user_email)
        return Favorite.list_favorites(user.id)

    @staticmethod
    def create_favorite(user_email: str, favorite_input: FavoriteInput
                        ) -> Favorite:
        user = User.get_user_by_email(user_email)
        created_favorite = Favorite(
            user_id=user.id, weather=favorite_input.weather,
            playlist=favorite_input.playlist)
        created_favorite.save()
        return created_favorite

    @staticmethod
    def delete_favorite(user_email: str, favorite_id) -> None:
        user = User.get_user_by_email(user_email)
        favorite = Favorite.get_by_id(favorite_id)

        if not favorite:
            raise HTTPException(status_code=404, detail='Favorite not found.')

        if favorite.user_id != user.id:
            raise HTTPException(status_code=403, detail='Forbidden.')

        favorite.delete()
