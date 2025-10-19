from typing import Dict, Optional
from app.domain.models import Note
from datetime import datetime

class InMemoryNoteRepository:
    def __init__(self):
        self._data: Dict[int, Note] = {}
        self._counter = 0

    def create(self, title: str, content: str) -> Note:
        self._counter += 1
        note = Note(
            id=self._counter,
            title=title,
            content=content,
            created_at=datetime.utcnow()
        )
        self._data[note.id] = note
        return note

    def get(self, note_id: int) -> Optional[Note]:
        return self._data.get(note_id)
