from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_and_get_note():
    # Create note
    resp = client.post("/notes", json={"title": "Hello", "content": "World"})
    assert resp.status_code in (200, 201)

    note = resp.json()
    assert "id" in note
    assert note["title"] == "Hello"
    assert note["content"] == "World"
    assert "created_at" in note

    # Get by id
    note_id = note["id"]
    get_resp = client.get(f"/notes/{note_id}")
    assert get_resp.status_code == 200

    got = get_resp.json()
    assert got["id"] == note_id
    assert got["title"] == "Hello"
    assert got["content"] == "World"


def test_get_nonexistent_note():
    resp = client.get("/notes/999999")
    assert resp.status_code == 404

    body = resp.json()
    assert "detail" in body
