# tests/test_app.py
from fastapi.testclient import TestClient

from tpp_mizan.app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to My Project API"}


def test_api_divide_success():
    response = client.get("/divide/10.0/2.0")
    assert response.status_code == 200
    assert response.json() == {"x": 10.0, "y": 2.0, "result": 5.0}


def test_api_divide_by_zero():
    response = client.get("/divide/10.0/0.0")
    # Verify it returns HTTP 400, not 500
    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot divide by zero"
