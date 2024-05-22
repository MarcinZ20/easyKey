import os
from datetime import datetime, timedelta, timezone

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from models import AccessTokenResponseModel, SearchModel
from token_cache import TokenCache

load_dotenv()
token_cache = TokenCache()

# Environmental variables
CLIENT_ID: str = os.getenv('CLIENT_ID')
CLIENT_SECRET: str = os.getenv('CLIENT_SECRET')

# Endpoints
SPOTIFY_TOKEN_URL:  str = 'https://accounts.spotify.com/api/token'
SPOTIFY_SEARCH_URL: str = 'https://accounts.spotify.com/v1/search'

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello there!"}

async def fetch_new_token() -> AccessTokenResponseModel:
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(SPOTIFY_TOKEN_URL, headers=headers, data=data)
    
    if response.status_code == 200:
        token_data = response.json()
        expiration_time = datetime.now(timezone.utc) + timedelta(seconds=token_data['expires_in'])
        token_cache.access_token = token_data['access_token']
        token_cache.expiration_time = expiration_time
        return AccessTokenResponseModel(**token_data)
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get('/get-token', response_model=AccessTokenResponseModel)
async def get_access_token():

    if token_cache.expiration_time is None or token_cache.expiration_time <= datetime.now(timezone.utc):
        return await fetch_new_token()

    return AccessTokenResponseModel(
        access_token=token_cache.access_token,
        token_type='Bearer',
        expires_in=int((token_cache.expiration_time - datetime.now(timezone.utc)).total_seconds())
    )


@app.get("/search-song", response_model=SearchModel)
async def search(search_model: SearchModel):

    headers = {
        'Authorization': 'Bearer'
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(SPOTIFY_SEARCH_URL, headers=headers, data=search_model)

        if response.status_code == 200:
            search_results = response.json()
            return search_results
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

@app.get("/token-cache")
async def get_token_parameters():
    return {'message': {
        'access_token': token_cache.access_token,
        'expires_at': token_cache.expiration_time
    }}