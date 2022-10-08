from fastapi import FastAPI, HTTPException, Body
from starlette.responses import Response
from pydantic import BaseModel

app = FastAPI()

class newUser(BaseModel):
    name: str = Body(default=...)
    email: str = Body(default=...)

@app.get("/")
def root():
    return {"message": "This is the root"}
