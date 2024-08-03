from fastapi import APIRouter, Depends

from app.schemas.favorite import FavoriteInput
from app.schemas.location import Location
from app.services.playlist_service import PlaylistService

router = APIRouter(prefix='/playlists', tags=['playlists'])


@router.get('/')
def get_playlists(location: Location = Depends()):
    playlist_service = PlaylistService()
    return playlist_service.get_playlist_by_location(location)


@router.post('/favorite')
def create_favorite(favorite: FavoriteInput):
    playlist_service = PlaylistService()
    return playlist_service.create_favorite(favorite)
