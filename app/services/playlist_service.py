from app.integrations.open_weather_api import OpenWeatherAPI
from app.integrations.spotify_api import SpotifyAPI
from app.schemas.location import Location
from app.schemas.playlists import Playlists, Playlist


class PlaylistService:
    open_weather_api: OpenWeatherAPI = OpenWeatherAPI()
    spotify_api: SpotifyAPI = SpotifyAPI()

    @classmethod
    def get_playlist_by_location(cls, location: Location):
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
            category=response.get('message'),
            playlists=[
                Playlist(
                    name=p.get('name'),
                    description=p.get('description'),
                    owner=p.get('owner').get('display_name'),
                    url=p.get('external_urls').get('spotify'),
                    image_url=p.get('images')[0].get('url') if p.get(
                        'images') else None
                ) for p in playlists]
        )
