from pydantic import BaseModel

class ProgramSchema(BaseModel):
    id: int
    name:str
    description:str
    hours:str