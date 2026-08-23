from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_project_success():
    payload = {
        "name": "Pembuatan Website TeFa",
        "client_name": "Dinas Pendidikan",
        "total_budget": 15000000.0
    }
    response = client.post("/projects/", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_create_project_invalid_budget():
    payload = {
        "name": "Proyek Tanpa Budget",
        "client_name": "Klien X",
        "total_budget": 0
    }
    response = client.post("/projects/", json=payload)
    assert response.status_code == 400