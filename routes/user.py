from fastapi import APIRouter
from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.user_database import Session, engine, Base
from jwt_manager import create_token, validate_token
from models.user_model import User as UserModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from schemas.user_scheme import User

user_router = APIRouter()

Base.metadata.create_all(bind=engine)

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

@user_router.get('/users', tags=['users'], response_model=List[User], status_code=200)
def get_users() -> List[User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.get('/users/{id}', tags=['users'], response_model=User)
def get_user(id: int = Path(ge=1, le=2000)) -> User:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "Usuario no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@user_router.get('/users/', tags=['users'], response_model=List[User])
def get_users_by_status(status: str = Query(min_length=5, max_length=20)) -> List[User]:
    db = Session()
    result = db.query(UserModel).filter(UserModel.status == status).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.post('/users', tags=['users'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    random_image_number = random.randint(1, 825)
    user.photo = f"https://rickandmortyapi.com/api/character/avatar/{random_image_number}.jpeg"
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el usuario"})

@user_router.put('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def update_user(id: int, user: User)-> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    result.username = user.username
    result.name = user.name
    result.last_name = user.last_name
    result.user_type = user.user_type
    result.password = user.password
    result.status = user.status
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el usuario"})

@user_router.delete('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def delete_user(id: int)-> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el usuario"})