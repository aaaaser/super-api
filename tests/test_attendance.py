def test_attendance_checkin_success(client):
    # 1. Buat project dulu agar foreign key project_id tersedia
    proj_res = client.post("/projects/", json={
        "name": "Proyek Absensi",
        "client_name": "Klien Absensi",
        "total_budget": 5000000.0
    })
    assert proj_res.status_code == 201
    project_id = proj_res.json()["id"]

    # 2. Lakukan check-in absensi dengan project_id tersebut
    response = client.post("/attendance/checkin", json={
        "student_id": "STD-001",
        "project_id": project_id
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["student_id"] == "STD-001"
    assert data["project_id"] == project_id
    assert data["status"] == "PRESENT"


def test_attendance_checkin_invalid_student(client):
    # Skenario ketika project_id tidak ditemukan
    response = client.post("/attendance/checkin", json={
        "student_id": "STD-999",
        "project_id": 99999
    })
    assert response.status_code == 404