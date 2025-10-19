from fastapi import FastAPI
from app.api import notes

app = FastAPI(title="QuickNotes API")

app.include_router(notes.router)
