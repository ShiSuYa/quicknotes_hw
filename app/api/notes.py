from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.note_service import NoteService
from app.infrastructure.repository import InMemoryNoteRepository

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
    created = service.create_note(note.title, note.content)
    return NoteResponse(**created.__dict__)

@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):
    found = service.get_note(note_id)
    if not found:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteResponse(**found.__dict__)
