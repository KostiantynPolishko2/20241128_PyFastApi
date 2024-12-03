from fastapi import HTTPException, status
from typing import List, Union, Annotated
from fastapi.params import Depends
from entities.models import Base
from entities.models import Program
from entities.schemas import ProgramSchema
from context.database import engine, SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

class ProgramService:

    def __init__(self):
        self.db: SessionLocal = get_db()

    def get_by_id(self, id: int):

        program = self.db.query(Program).filter(Program.id == id).first()
        if not program:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Program with id {id} not found!')
        return program

    # def add(self, note_in: NoteIn)->dict[str:int]:
    #     self.is_title_exist(note_in.title)
    #     note = Note(id=notes[len(notes)-1].id+1, title=note_in.title, description=note_in.description)
    #     notes.append(note)
    #
    #     return {"response": status.HTTP_201_CREATED}
