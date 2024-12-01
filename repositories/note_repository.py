from fastapi import HTTPException, status
from typing import List, Dict
from entities import Note
from context import notes

def get_notes()-> List[Note] | HTTPException:
    if len(notes) == 0:
        raise HTTPException(status_code=404, detail='not found')

    return notes

def get_note_by_id(id: int)->Note | HTTPException:

    for note in notes:
        if id == note.id:
            return note

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note id {id} not found!')

def is_title_exist(title: str)->HTTPException | None:

    _title = title.lower()

    for note in notes:
        if _title == note.title.lower():
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'note title \"{title}\" is already exist in db')

    return None

def add_note(note: Note)->HTTPException | dict[str:int]:
    is_title_exist(note.title)

    note.id = notes[len(notes)-1].id+1
    notes.append(note)

    return {"response": status.HTTP_201_CREATED}

def update_note(id: int, new_note: Note)->HTTPException | dict[str:int]:

    for note in notes:
        if id == note.id:
            note = new_note
            note.id = id
            return {"response": status.HTTP_202_ACCEPTED}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note id {id} not found!')

def delete_note(id: int)->HTTPException | dict[str:int]:
    if len(notes)==0:
        raise HTTPException(status_code=404, detail='not found')

    for note in notes:
        if id == note.id:
            notes.remove(note)
            return {"response": status.HTTP_205_RESET_CONTENT}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note id {id} not found!')