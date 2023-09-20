from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from config.database import Session, engine, Base
from models.user import User as UserModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
import random

app = FastAPI()
app.title = "Mi aplicación con  FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)


class User(BaseModel):
    email:str
    password:str

class User(BaseModel):
    id: Optional[int] = None
    username: str = Field(min_length=5, max_length=20)
    name: str = Field(min_length=2, max_length=50)
    last_name: str = Field(min_length=2, max_length=50)
    user_type: str = Field(min_length=2, max_length=20)
    password: str = Field(min_length=8, max_length=50)
    status: str = Field(min_length=2, max_length=20)
    photo: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "username": "example_username",
                "name": "John",
                "last_name": "Doe",
                "user_type": "admin",
                "password": "example_password",
                "status": "active",
                "photo": "https://rickandmortyapi.com/api/character/avatar/361.jpeg"
            }
        }


@app.get('/', tags=['home'])
def message():
    with open('index.html', 'r') as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

@app.get('/users', tags=['users'], response_model=List[User], status_code=200)
def get_users() -> List[User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.get('/users/{id}', tags=['users'], response_model=User)
def get_user(id: int = Path(ge=1, le=2000)) -> User:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "Usuario no encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.get('/users/', tags=['users'], response_model=List[User])
def get_users_by_status(status: str = Query(min_length=5, max_length=20)) -> List[User]:
    db = Session()
    result = db.query(UserModel).filter(UserModel.status == status).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@app.post('/users', tags=['users'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    random_image_number = random.randint(1, 825)
    user.photo = f"https://rickandmortyapi.com/api/character/avatar/{random_image_number}.jpeg"
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el usuario"})

@app.put('/users/{id}', tags=['users'], response_model=dict, status_code=200)
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

@app.delete('/users/{id}', tags=['users'], response_model=dict, status_code=200)
def delete_user(id: int)-> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el usuario"})