from pydantic import BaseModel

class MessageCreate(BaseModel):
    prompt: str

class MessageRead(BaseModel):
    id: int
    prompt: str
    response: str

    class Config:
        orm_mode = True
