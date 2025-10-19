from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_get_note():
    response = client.post("/notes", json={"title": "Hello", "content": "World"})
    assert response.status_code == 200
    note = response.json()
    assert note["title"] == "Hello"
    assert note["content"] == "World"
    assert "id" in note
    assert "created_at" in note

    get_resp = client.get(f"/notes/{note['id']}")
    assert get_resp.status_code == 200
    fetched = get_resp.json()
    assert fetched["title"] == "Hello"
    assert fetched["content"] == "World"
    assert fetched["id"] == note["id"]

def test_get_nonexistent_note():
    response = client.get("/notes/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"
