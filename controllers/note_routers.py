from fastapi import APIRouter, status, HTTPException, Depends, Path, Body
from typing import List, Annotated, Any

from websockets.http11 import Response

from entities import NoteIn, Note, UpdateNote
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


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Note])
async def get_notes(note_service: note_service_dependency)->List[Note]:
    return note_service.get()


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Note)
async def get_note_by_id(id: id_params, note_service: note_service_dependency)->Note:
    return note_service.get_by_id(id)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_note(note_service: note_service_dependency, note_in: NoteIn = Body(embeded = True))->Any:
    if not note_in:
        raise HTTPException(status_code=400, detail='bad request')

    return note_service.add(note_in)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_note(id: id_params, note_in: NoteIn, note_service: note_service_dependency):
    if not note_in:
        raise HTTPException(status_code=400, detail='bad request')

    return note_service.update(id, note_in)


@router.patch("/{id}", status_code=status.HTTP_202_ACCEPTED)
async def modify_note(id: id_params, updateNote: UpdateNote, note_service: note_service_dependency):
    if not updateNote:
        raise HTTPException(status_code=400, detail='bad request')

    return note_service.modify(id, updateNote)

@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_note(id: id_params, note_service: note_service_dependency):
    return note_service.delete(id)
