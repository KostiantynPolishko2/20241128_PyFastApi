from typing import Optional
from pydantic import BaseModel, Field

class NoteIn(BaseModel):
    title: str = Field(description='language name', min_length=1, max_length=10)
    description: str = Field(max_length=30)

class Note(NoteIn):
    id:int = Field(description='id remain equal 0')

class UpdateNote(BaseModel):
    description: Optional[str] = None
