from fastapi import APIRouter, status, HTTPException, Depends
from typing import List, Annotated
from entities import Note
from services.note_service import NoteService

router = APIRouter(
    prefix='/api/v1',
    tags=['Http request: Note'],
    # responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

def get_note_service()->NoteService:
    return NoteService()

note_service_dependency = Annotated[NoteService, Depends(get_note_service)]


@router.get("/", status_code=status.HTTP_200_OK)
async def get_notes(note_service: note_service_dependency)->List[Note]:
    return note_service.get_notes()


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_note_by_id(id: int, note_service: note_service_dependency)->Note:
    return note_service.get_note_by_id(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_note(note: Note, note_service: note_service_dependency):
    if note == None:
        raise HTTPException(status_code=400, detail='bad request')

    return note_service.add_note(note)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_note(id: int, note: Note, note_service: note_service_dependency):
    if note == None:
        raise HTTPException(status_code=400, detail='bad request')

    return note_service.update_note(id, note)


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_note(id: int, note_service: note_service_dependency):
    return note_service.delete_note(id)