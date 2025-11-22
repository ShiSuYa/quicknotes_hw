from datetime import datetime
from pydantic import BaseModel, model_serializer

class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime

    @model_serializer(mode="wrap")
    def serialize_created_at(self, value: datetime) -> str:
        return value.isoformat()
