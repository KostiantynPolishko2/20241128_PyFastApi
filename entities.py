from typing import Optional
from pydantic import BaseModel, Field

class Note(BaseModel):
    id:int = Field(description='id remain equal 0')
    title: str = Field(description='language name', min_length=1, max_length=10)
    description: str = Field(max_length=30)

class UpdateNote(BaseModel):
    description: Optional[str] = None