from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_attendance_checkin_success():
    payload = {"student_id": 12, "project_id": 101}
    response = client.post("/attendance/check-in", json=payload)
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_attendance_checkin_invalid_student():
    payload = {"student_id": 0, "project_id": 101}
    response = client.post("/attendance/check-in", json=payload)
    assert response.status_code == 400