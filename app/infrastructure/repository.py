from datetime import datetime
from app.domain.models import NoteResponse

class Note:
    _id_counter = 1

    def __init__(self, title: str, content: str):
        self.id = Note._id_counter
        Note._id_counter += 1
        self.title = title
        self.content = content
        self.created_at = datetime.utcnow()

notes_db = []

def add_note(title: str, content: str) -> Note:
    note = Note(title, content)
    notes_db.append(note)
    return note

def get_note(note_id: int) -> Note | None:
    for note in notes_db:
        if note.id == note_id:
            return note
    return None
