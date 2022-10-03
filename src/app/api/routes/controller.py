from fastapi import FastAPI, HTTPException
from starlette.responses import Response


app = FastAPI()


@app.get("/")
def root():
    return {"message": "This is the root"}
