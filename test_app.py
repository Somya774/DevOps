import pytest
import json
from app.main import app  # Assuming your Flask app is in app.main

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_predict(client):
    response = client.post(
        '/predict',
        json={'features': [5.1, 3.5, 1.4, 0.2]},
        content_type='application/json'
    )
    assert response.status_code == 200
    assert 'prediction' in json.loads(response.data)  # Check if the response contains prediction
