import pytest

def pytest_configure():
    pytest.token = ''
    pytest.weather = dict()
    pytest.playlists = dict()
    pytest.favorite_id = ''
