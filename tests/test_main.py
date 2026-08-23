# tests/test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# 1. Test Endpoint Root
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

# 2. Test Auth Login (Sukses)
# Catatan: services.py mengecek username == "user_demo" dan password == "password123"
def test_auth_login_success():
    payload = {"username": "user_demo", "password": "password123"}
    response = client.post("/auth/login", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert "user_id" in data["data"]

# 3. Test Auth Login (Gagal)
def test_auth_login_failed():
    payload = {"username": "user_demo", "password": "salah_password"}
    response = client.post("/auth/login", json=payload)
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Username atau password salah"

# 4. Test Payment Checkout (Sukses)
def test_payment_checkout_success():
    payload = {"user_id": 101, "amount": 50000.0, "method": "QRIS"}
    response = client.post("/payments/checkout", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["data"]["amount"] == 50000.0

# 5. Test Payment Checkout (Nominal Invalid)
def test_payment_checkout_invalid_amount():
    payload = {"user_id": 101, "amount": 0, "method": "QRIS"}
    response = client.post("/payments/checkout", json=payload)
    
    assert response.status_code == 400
    assert "Nominal pembayaran harus lebih besar dari 0" in response.json()["detail"]