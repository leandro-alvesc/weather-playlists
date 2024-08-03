from fastapi import FastAPI, status
from firedantic import configure

from .api.v1 import playlists, users, auth
from .firestore import get_firestore_client
from .logger import get_logger
from .schemas.health_check import HealthCheck
from .schemas.info import Info

logger = get_logger()
logger.info('Starting Weather Playlists API...')

app = FastAPI(title='api')

db_client = get_firestore_client()
configure(db_client)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(playlists.router)

@app.get('/health',
         tags=['healthcheck'],
         status_code=status.HTTP_200_OK,
         response_model=HealthCheck)
def get_health() -> HealthCheck:
    return HealthCheck()


@app.get('/info',
         tags=['info'],
         status_code=status.HTTP_200_OK,
         response_model=Info)
def get_info() -> Info:
    return Info()
