from fastapi import FastAPI, status, HTTPException
from typing import List
from entities import Note
from context import notes

# server gateway initialization
app = FastAPI(title='NotesApi',
              description='WebApi CRUD of Note entities',
              version='1.0.0',
              docs_url='/swagger',
              contact={
                  'name': 'itstep academy',
                  'url': 'https://itstep.dp.ua',
                  'email': 'polxs_wp31@student.itstep.org'
              })


@app.get("/notes", status_code=status.HTTP_200_OK)
async def get_notes()->List[Note]:

    if len(notes) == 0:
        raise HTTPException(status_code=404, detail='not found')

    return notes


@app.post("/notes", status_code=status.HTTP_201_CREATED)
async def create_note(note: Note):
    if note == None:
        raise HTTPException(status_code=400, detail='bad request')

    note.id = notes[len(notes)-1].id+1

    notes.append(note)

    return {"response" : status.HTTP_201_CREATED}


@app.put("/notes/{id}", status_code=status.HTTP_202_ACCEPTED)
async def update_note(id: int, note: Note):

    if note == None:
        raise HTTPException(status_code=400, detail='bad request')

    is_no_id = True
    for _note in notes:
        if id == _note.id:
            is_no_id = False
            _note.title = note.title
            _note.description = note.description

    if is_no_id:
        raise HTTPException(status_code=400, detail='bad request')

    return {"response" : status.HTTP_202_ACCEPTED}


@app.delete("/notes/{id}", status_code=status.HTTP_200_OK)
async def delete_note(id: int):

    _id:int = abs(id)
    if len(notes)==0:
        raise HTTPException(status_code=404, detail='not found')

    is_no_id = True
    for note in notes:
        if id == note.id:
            is_no_id = False
            notes.remove(note)

    if is_no_id:
        raise HTTPException(status_code=400, detail='bad request')

    return {"response" : status.HTTP_200_OK}