from fastapi import FastAPI, status
from functools import lru_cache

from .api.v1 import playlists
from .config import Settings
from .models.health_check import HealthCheck
from .models.info import Info


app = FastAPI()

@lru_cache
def get_settings():
    return Settings()

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
