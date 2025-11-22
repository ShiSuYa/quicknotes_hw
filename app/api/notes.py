from fastapi import APIRouter, HTTPException
from app.domain.models import NoteCreate, NoteResponse
from app.services import note_service as service

router = APIRouter()

@router.post("/notes", response_model=NoteResponse)
def create_note(note: NoteCreate):
    created = service.create_note(note.title, note.content)
    return NoteResponse(**created.__dict__)

@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):
    note = service.get_note_by_id(note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return NoteResponse(**note.__dict__)
