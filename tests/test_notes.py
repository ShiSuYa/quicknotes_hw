from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_note():
    response = client.post("/notes", json={"title": "Hello", "content": "World"})
    assert response.status_code == 200
    note = response.json()
    assert note["title"] == "Hello"

    get_resp = client.get(f"/notes/{note['id']}")
    assert get_resp.status_code == 200
    fetched = get_resp.json()
    assert fetched["content"] == "World"
