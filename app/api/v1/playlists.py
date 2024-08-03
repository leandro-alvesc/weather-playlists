from fastapi import APIRouter, Depends
from typing import Annotated, List

from app.schemas.favorite import FavoriteInput, FavoriteOutput
from app.schemas.location import Location
from app.schemas.playlists import Playlists
from app.services.playlist_service import PlaylistService
from app.utils.auth_utils import AuthUtils

router = APIRouter(prefix='/playlists', tags=['playlists'])


@router.get('/', response_model=Playlists)
def get_playlists(location: Location = Depends()):
    playlist_service = PlaylistService()
    return playlist_service.get_playlist_by_location(location)


@router.get('/favorites', response_model=List[FavoriteOutput])
def list_favorites(email: Annotated[str, Depends(
                  AuthUtils.get_user_email_from_token)]):
    playlist_service = PlaylistService()
    return [f.to_schema() for f in playlist_service.list_favorites(email)]


@router.post('/favorites', response_model=FavoriteOutput)
def create_favorite(favorite: FavoriteInput, email: Annotated[str, Depends(
                    AuthUtils.get_user_email_from_token)]):
    playlist_service = PlaylistService()
    return playlist_service.create_favorite(email, favorite).to_schema()


@router.delete('/favorites/{favorite_id}')
def create_favorite(favorite_id: str, email: Annotated[str, Depends(
                    AuthUtils.get_user_email_from_token)]):
    playlist_service = PlaylistService()
    return playlist_service.delete_favorite(email, favorite_id)
