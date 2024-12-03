from fastapi import APIRouter, status, HTTPException, Depends, Path, Body, Response
from typing import List, Annotated, Any

from entities.schemas import ProgramSchema
from services.program_service import ProgramService
from entities.models import Program

router = APIRouter(
    prefix='/api/v1',
    tags=['Http request: Program'],
    responses={status.HTTP_400_BAD_REQUEST: {'description' : 'Bad Request'}}
)

def get_program_service()->ProgramService:
    return ProgramService()

program_service_dependency = Annotated[ProgramService, Depends(get_program_service)]
id_params = Annotated[int, Path(description='id of Program', ge=1)]

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=ProgramSchema)
async def get_program_by_id(id: id_params, program_service: program_service_dependency):
    return program_service.get_by_id(id)
#
#
# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def add_note(note_service: note_service_dependency, note_in: NoteIn = Body(embeded = True))->Any:
#     if not note_in:
#         raise HTTPException(status_code=400, detail='bad request')
#
#     return note_service.add(note_in)
