import logging
from app.domain.models import Note
from app.infrastructure.repository import InMemoryNoteRepository

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

class NoteService:
    def __init__(self, repo: InMemoryNoteRepository):
        self.repo = repo
        self.create_counter = 0

    def create_note(self, title: str, content: str) -> Note:
        self.create_counter += 1
        logger.info(f"Создание заметки: {title}")
        return self.repo.create(title, content)

    def get_note(self, note_id: int) -> Note | None:
        logger.info(f"Получение заметки с ID: {note_id}")
        return self.repo.get(note_id)
