from datetime import datetime
from pydantic import BaseModel, model_serializer

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    @model_serializer(mode="json")
    def serialize_created_at(self, value: datetime) -> str:
        return value.isoformat()
