from typing import List

from pydantic import BaseModel


class AccessTokenResponseModel(BaseModel):
    access_token: str = None
    token_type: str = None
    expires_in: int = None


class SearchModel(BaseModel):
    track: str = None
    artist: str = None
    album: str = None
