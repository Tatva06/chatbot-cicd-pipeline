from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_chat_ping():
    res = client.post("/chat", json={"message": "ping"})
    assert res.status_code == 200
    assert res.json()["reply"] == "pong"