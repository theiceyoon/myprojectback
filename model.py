from pydantic import BaseModel

class Name(BaseModel):
    name: str

class Message(BaseModel):
    message: str

class Entry(BaseModel):
    name: str
    message: str