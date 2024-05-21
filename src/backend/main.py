from pathlib import Path
from typing import Dict, List

from fastapi import FastAPI
from models import SearchModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world!"}

@app.get("/search/", response_model=SearchModel)
async def search(model: SearchModel):
    return model
