from app.domain.models import Note
from app.infrastructure.repository import InMemoryNoteRepository

class NoteService:
    def __init__(self, repo: InMemoryNoteRepository):
        self.repo = repo

    def create_note(self, title: str, content: str) -> Note:
        return self.repo.create(title, content)

    def get_note(self, note_id: int) -> Note | None:
        return self.repo.get(note_id)
