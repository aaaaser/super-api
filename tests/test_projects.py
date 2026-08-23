def test_create_project_success(client):
    response = client.post("/projects/", json={
        "name": "Sistem Informasi Kasir",
        "client_name": "PT Maju Jaya",
        "total_budget": 15000000.0
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Sistem Informasi Kasir"
    assert data["client_name"] == "PT Maju Jaya"
    assert data["total_budget"] == 15000000.0
    assert "id" in data


def test_get_projects_list(client):
    # Buat 1 proyek terlebih dahulu
    client.post("/projects/", json={
        "name": "Aplikasi E-Commerce",
        "client_name": "Toko Berkah",
        "total_budget": 8000000.0
    })

    # Ambil daftar proyek
    response = client.get("/projects/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_get_project_not_found(client):
    response = client.get("/projects/99999")
    assert response.status_code == 404