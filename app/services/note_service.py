from app.infrastructure.repository import add_note, get_note

def create_note(title: str, content: str):
    return add_note(title, content)

def get_note_by_id(note_id: int):
    return get_note(note_id)
