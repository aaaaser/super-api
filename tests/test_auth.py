from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_login_success():
    payload = {"username": "user_demo", "password": "password123"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_login_wrong_password():
    payload = {"username": "user_demo", "password": "salah_password"}
    response = client.post("/auth/login", json=payload)
    assert response.status_code == 400