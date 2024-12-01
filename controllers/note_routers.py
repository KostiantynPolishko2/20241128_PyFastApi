from fastapi import APIRouter, status, HTTPException
from typing import List
from entities import Note
from repositories import note_repository

router = APIRouter(
    prefix='/api/v1',
    tags=['Http request: Note'],
    # responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_notes()->List[Note]:
    return note_repository.get_notes()

@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_note_by_id(id: int)->Note:
    return note_repository.get_note_by_id(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_note(note: Note):
    if note == None:
        raise HTTPException(status_code=400, detail='bad request')

    return note_repository.add_note(note)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_note(id: int, note: Note):

    if note == None:
        raise HTTPException(status_code=400, detail='bad request')

    return note_repository.update_note(id, note)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_note(id: int):
    return note_repository.delete_note(id)