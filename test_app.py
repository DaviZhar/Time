import pytest
from main import main

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_time_route(client):
    response = client.get('/time')
    data = response.get_json()
    assert response.status_code == 200
    assert data['time'] > 0
