import pytest
import os
from fastapi.testclient import TestClient
os.environ['FIRESTORE_EMULATOR_HOST'] = 'localhost:8686'

from app.main import app
from app.config import get_settings

client = TestClient(app)
settings = get_settings()

USER_INFO = dict(name='User Test', email='test@user.com', password='passtest')
LOCATION_INFO = dict(city_name='São Paulo', country_code='BR')


def test_info():
    response = client.get("/info")
    assert response.status_code == 200
    assert response.json() == dict(
        app_name=settings.app_name, developer_email=settings.developer_email)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == dict(status='OK')


def test_create_user():
    response = client.post('/users/', json=USER_INFO)
    assert response.status_code == 200
    user = response.json()
    assert user.get('name') == USER_INFO.get('name')
    assert user.get('email') == USER_INFO.get('email')


def test_auth_user():
    data = dict(username=USER_INFO.get('email'),
                password=USER_INFO.get('password'))
    response = client.post('/auth/login', data=data)
    assert response.status_code == 200
    assert 'access_token' in response.json()
    pytest.token = response.json().get('access_token')


def test_get_playlists():
    response = client.get('playlists/', params=LOCATION_INFO,
                          headers=dict(token=pytest.token))
    assert response.status_code == 200
    data = response.json()
    playlist = next((p for p in data.get('playlists', [])), None)
    weather = data.get('weather')
    assert playlist and weather
    pytest.playlist = playlist
    pytest.weather = weather


def test_favorite_playlists():
    data = dict(weather=pytest.weather, playlist=pytest.playlist)
    response = client.post('playlists/favorites', json=data,
                           headers=dict(token=pytest.token))
    assert response.status_code == 200
    pytest.favorite_id = response.json().get('id')


def test_get_favorite_playlists():
    response = client.get('playlists/favorites',
                          headers=dict(token=pytest.token))
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_delete_favorite_playlist():
    response = client.delete(f'playlists/favorites/{pytest.favorite_id}',
                          headers=dict(token=pytest.token))
    assert response.status_code == 200
