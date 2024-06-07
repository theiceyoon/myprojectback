from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Name(BaseModel):
    name: str

class Message(BaseModel):
    message: str

class Entry(BaseModel):
    name: str
    message: str

guestbook = {
    "entries": []  # 이름과 메시지를 함께 저장
}

@router.post("/names")
async def add_name(name: Name) -> dict:
    guestbook["entries"].append({"name": name.name, "message": ""})
    return {"msg": "Name added"}

@router.get("/names")
async def retrieve_names() -> dict:
    names = [entry["name"] for entry in guestbook["entries"]]
    return {"names": names}

@router.post("/messages")
async def add_message(message: Message) -> dict:
    guestbook["entries"].append({"name": "", "message": message.message})
    return {"msg": "Message added"}

@router.get("/messages")
async def retrieve_messages() -> dict:
    messages = [entry["message"] for entry in guestbook["entries"]]
    return {"messages": messages}

@router.post("/entry")
async def add_entry(entry: Entry) -> dict:
    guestbook["entries"].append({"name": entry.name, "message": entry.message})
    return {"msg": "Entry added"}

@router.delete("/entry")
async def delete_entry(entry: Entry) -> dict:
    try:
        guestbook["entries"].remove({"name": entry.name, "message": entry.message})
        return {"msg": "Entry deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Entry not found")


@router.get("/entry")
async def retrieve_entries() -> dict:
    return {"entries": guestbook["entries"]}
