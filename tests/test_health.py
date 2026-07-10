from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_me_no_key():
    response = client.get("/me")
    assert response.status_code == 422

def test_me_wrong_key():
    response = client.get("/me", headers={"X-API-Key": "wrongkey"})
    assert response.status_code == 401
