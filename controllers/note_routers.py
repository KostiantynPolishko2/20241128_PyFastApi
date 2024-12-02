from fastapi import APIRouter, status, HTTPException, Depends, Path, Body
from typing import List, Annotated
from entities import Note, UpdateNote
from services.note_service import NoteService

router = APIRouter(
    prefix='/api/v1',
    tags=['Http request: Note'],
    # responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

def get_note_service()->NoteService:
    return NoteService()

note_service_dependency = Annotated[NoteService, Depends(get_note_service)]
id_params = Annotated[int, Path(description='id of Note', ge=1)]

@router.get("/", status_code=status.HTTP_200_OK)
async def get_notes(note_service: note_service_dependency)->List[Note]:
    return note_service.get()


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_note_by_id(id: id_params, note_service: note_service_dependency)->Note:
    return note_service.get_by_id(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_note(note_service: note_service_dependency, note: Note = Body(embeded = True)):
    if note == None:
        raise HTTPException(status_code=400, detail='bad request')

    return note_service.add(note)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_note(id: id_params, note: Note, note_service: note_service_dependency):
    if note == None:
        raise HTTPException(status_code=400, detail='bad request')

    return note_service.update(id, note)


@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def modify_note(id: id_params, updateNote: UpdateNote, note_service: note_service_dependency):
    if updateNote == None:
        raise HTTPException(status_code=400, detail='bad request')

    return note_service.modify(id, updateNote)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_note(id: id_params, note_service: note_service_dependency):
    return note_service.delete(id)