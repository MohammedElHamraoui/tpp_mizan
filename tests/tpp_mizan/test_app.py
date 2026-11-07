# tests/tpp_mizan/test_app.py
import pytest
from fastapi.testclient import TestClient

from tpp_mizan.app import app


@pytest.fixture
def client():
    # The 'with' block is what actually triggers the FastAPI lifespan (startup/shutdown)
    with TestClient(app) as c:
        yield c


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to TPP Mizan API"}


def test_api_add(client):
    response = client.get("/add/10.0/2.0")
    assert response.status_code == 200
    assert response.json() == {"operation": "add", "x": 10.0, "y": 2.0, "result": 12.0}


def test_api_subtract(client):
    response = client.get("/subtract/10.0/2.0")
    assert response.status_code == 200
    assert response.json() == {"operation": "subtract", "x": 10.0, "y": 2.0, "result": 8.0}


def test_api_multiply(client):
    response = client.get("/multiply/10.0/2.0")
    assert response.status_code == 200
    assert response.json() == {"operation": "multiply", "x": 10.0, "y": 2.0, "result": 20.0}


def test_api_divide_success(client):
    response = client.get("/divide/10.0/2.0")
    assert response.status_code == 200
    assert response.json() == {"operation": "divide", "x": 10.0, "y": 2.0, "result": 5.0}


def test_api_divide_by_zero(client):
    response = client.get("/divide/10.0/0.0")
    assert response.status_code == 400
    assert response.json()["detail"] == "Cannot divide by zero"
