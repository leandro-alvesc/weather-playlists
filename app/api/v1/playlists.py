from fastapi import APIRouter, Depends

from app.schemas.favorite import FavoriteInput, FavoriteOutput
from app.schemas.location import Location
from app.schemas.playlists import Playlists
from app.services.playlist_service import PlaylistService

router = APIRouter(prefix='/playlists', tags=['playlists'])


@router.get('/', response_model=Playlists)
def get_playlists(location: Location = Depends()):
    playlist_service = PlaylistService()
    return playlist_service.get_playlist_by_location(location)


@router.post('/favorite', response_model=FavoriteOutput)
def create_favorite(favorite: FavoriteInput):
    playlist_service = PlaylistService()
    return playlist_service.create_favorite(favorite)
