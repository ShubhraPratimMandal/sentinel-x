from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "operational"

def test_overview():
    response = client.get("/api/v1/system/overview")
    assert response.status_code == 200
    assert response.json()["threat_posture"] > 0

def test_indicator_lookup():
    response = client.get("/api/v1/indicators/IOC-0001")
    assert response.status_code == 200
    assert response.json()["severity"] == "CRITICAL"

def test_search():
    response = client.get("/api/v1/search?q=credential")
    assert response.status_code == 200
    assert len(response.json()["alerts"]) >= 1
