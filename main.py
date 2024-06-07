from fastapi import FastAPI
from guestbook import router as guestbook_router
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = ["http://127.0.0.1:5500", "http://50.19.18.53/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
@app.get("/")
async def welcome() -> dict:
    return {"msg": "hi"}

app.include_router(guestbook_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8005, reload=True)
