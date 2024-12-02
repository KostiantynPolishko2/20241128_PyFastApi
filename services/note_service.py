from fastapi import HTTPException, status
from typing import List, Union
from entities import NoteIn, Note, UpdateNote
from context import notes

class NoteService:

    def is_title_exist(self, title: str)->None:
        _title = title.lower()

        for note in notes:
            if _title == note.title.lower():
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail=f'note title \"{title}\" is already exist in db')

        return None

    def get(self)-> List[Note]:
        if not notes:
            raise HTTPException(status_code=404, detail='not found')

        return notes

    def get_by_id(self, id: int)->Note:
        for note in notes:
            if id == note.id:
                return note

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note id {id} not found!')

    def add(self, note_in: NoteIn)->dict[str:int]:
        self.is_title_exist(note_in.title)
        note = Note(id=notes[len(notes)-1].id+1, title=note_in.title, description=note_in.description)
        notes.append(note)

        return {"response": status.HTTP_201_CREATED}

    def update(self, id: int, new_note_in: NoteIn)->dict[str:int]:
        for index, note in enumerate(notes):
            if note.id == id:
                notes[index] = Note(id=id, title=new_note_in.title, description=new_note_in.description)
                return {"response": status.HTTP_202_ACCEPTED}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note id {id} not found!')

    def delete(self, id: int)->dict[str:int]:

        for note in notes:
            if id == note.id:
                notes.remove(note)
                return {"response": status.HTTP_205_RESET_CONTENT}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note id {id} not found!')

    def modify(self, id: int, update_note: UpdateNote)->dict[str:int]:
        if len(notes)==0:
            raise HTTPException(status_code=404, detail='not found')

        for index, note in enumerate(notes):
            if id == note.id:
                update_data = update_note.model_dump(exclude_unset=True)
                notes[index] = notes[index].model_copy(update=update_data)

                return {"response": status.HTTP_202_ACCEPTED}

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Note id {id} not found!')