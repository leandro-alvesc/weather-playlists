from fastapi import APIRouter

router = APIRouter(
    prefix='/playlists',
    tags=['playlists']
)

@router.get('/')
def get_playlists(city: str):
    return dict(data=city)
