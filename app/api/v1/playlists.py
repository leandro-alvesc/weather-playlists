from fastapi import APIRouter, Depends

from app.services.playlist_service import PlaylistService
from app.schemas.location import Location

router = APIRouter(
    prefix='/playlists',
    tags=['playlists']
)


@router.get('/')
def get_playlists(location: Location = Depends()):
    playlist_service = PlaylistService()
    return playlist_service.get_playlist_by_location(location)
