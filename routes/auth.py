from fastapi import APIRouter
from pydantic import BaseModel
from jwt_manager import create_token
from schemas.auth import Auth

auth_router = APIRouter()

@auth_router.post('/login', tags=['auth'])
def login(user: Auth):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)