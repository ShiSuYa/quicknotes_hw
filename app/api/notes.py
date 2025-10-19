from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.note_service import NoteService
from app.infrastructure.repository import InMemoryNoteRepository
import logging

logger = logging.getLogger(__name__)

router = APIRouter()
service = NoteService(InMemoryNoteRepository())

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: str

@router.post("/notes", response_model=NoteResponse)
def create_note(note: NoteCreate):
    logger.info(f"API: запрос на создание заметки '{note.title}'")
    created = service.create_note(note.title, note.content)
    return NoteResponse(**created.__dict__)

@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):
    logger.info(f"API: запрос на получение заметки ID={note_id}")
    found = service.get_note(note_id)
    if not found:
        logger.warning(f"API: заметка ID={note_id} не найдена")
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteResponse(**found.__dict__)
