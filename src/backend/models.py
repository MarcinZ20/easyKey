from pydantic import BaseModel


class AccessTokenResponseModel(BaseModel):
    access_token: str = None
    token_type: str = None
    expires_in: int = None
