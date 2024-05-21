from typing import List

from pydantic import BaseModel


class SearchModel(BaseModel):
    title: str = None
    artists: List[str] = None
    album: str = None


class Song(BaseModel):
    title: str = None
    artist: List[str] = None
    album: str = None
    date_released: str = None
