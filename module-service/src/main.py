from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from config.database import Session, engine, Base
from models.module import Module as ModuleModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer

app = FastAPI()
app.title = "Module Microserivice"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)


class User(BaseModel):
    email:str
    password:str

class Module(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=5, max_length=15)
    description: str = Field(min_length=15, max_length=50)
    module_type: str = Field(min_length=15, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Module_test",
                "description": "Descripción del modulo",
                "module_type": "Finance"
            }
        }

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world from Module</h1>')


@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(user.dict())
        return JSONResponse(status_code=200, content=token)

@app.get('/modules', tags=['modules'], response_model=List[Module], status_code=200, dependencies=[Depends(JWTBearer())])
def get_modules() -> List[Module]:
    db = Session()
    result = db.query(ModuleModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.get('/modules/{id}', tags=['modules'], response_model=Module)
def get_module(id: int = Path(ge=1, le=2000)) -> Module:
    db = Session()
    result = db.query(ModuleModel).filter(ModuleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.get('/modules/', tags=['modules'], response_model=List[Module])
def get_modules_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Module]:
    db = Session()
    result = db.query(ModuleModel).filter(ModuleModel.category == category).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@app.post('/modules', tags=['modules'], response_model=dict, status_code=201)
def create_module(module: Module) -> dict:
    db = Session()
    new_module = ModuleModel(**module.dict())
    db.add(new_module)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el módulo"})

@app.put('/modules/{id}', tags=['modules'], response_model=dict, status_code=200)
def update_module(id: int, module: Module)-> dict:
    db = Session()
    result = db.query(ModuleModel).filter(ModuleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    result.title = module.title
    result.overview = module.overview
    result.year = module.year
    result.rating = module.rating
    result.category = module.category
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el módulo"})

@app.delete('/modules/{id}', tags=['modules'], response_model=dict, status_code=200)
def delete_module(id: int)-> dict:
    db = Session()
    result = db.query(ModuleModel).filter(ModuleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el módulo"})