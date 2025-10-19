from fastapi import APIRouter, HTTPException
from typing import List
from domain.models import Note, NoteCreate
from services.note_service import NoteService

router = APIRouter(prefix="/notes", tags=["notes"])
service = NoteService()

@router.post("/", response_model=Note)
def create_note_endpoint(payload: NoteCreate):
    """
    Endpoint для создания заметки.
    Здесь можно добавить логирование и метрики (см. комментарии ниже).
    """
    note = service.create_note(payload)
    return note

@router.get("/", response_model=List[Note])
def list_notes_endpoint():
    """
    Endpoint для получения всех заметок.
    Здесь можно добавить подсчёт метрик (например, время ответа).
    """
    return service.get_all()
