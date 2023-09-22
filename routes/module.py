from fastapi import APIRouter
from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.module_database import Session, engine, Base
from jwt_manager import create_token, validate_token
from models.module_model import Module as ModuleModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from schemas.module_scheme import Module

module_router = APIRouter()

Base.metadata.create_all(bind=engine)

@module_router.get('/modules', tags=['Modules'], response_model=List[Module], status_code=200)
def get_modules() -> List[Module]:
    db = Session()
    result = db.query(ModuleModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@module_router.get('/modules/{id}', tags=['Modules'], response_model=Module)
def get_module(id: int = Path(ge=1, le=2000)) -> Module:
    db = Session()
    result = db.query(ModuleModel).filter(ModuleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@module_router.get('/modules/', tags=['Modules'], response_model=List[Module])
def get_modules_by_category(category: str = Query(min_length=5, max_length=15)) -> List[Module]:
    db = Session()
    result = db.query(ModuleModel).filter(ModuleModel.category == category).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@module_router.post('/modules', tags=['Modules'], response_model=dict, status_code=201)
def create_module(module: Module) -> dict:
    db = Session()
    new_module = ModuleModel(**module.dict())
    db.add(new_module)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el módulo"})

@module_router.put('/modules/{id}', tags=['Modules'], response_model=dict, status_code=200)
def update_module(id: int, module: Module)-> dict:
    db = Session()
    result = db.query(ModuleModel).filter(ModuleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    result.name = module.name
    result.description = module.description
    result.module_type = module.module_type
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el módulo"})

@module_router.delete('/modules/{id}', tags=['Modules'], response_model=dict, status_code=200)
def delete_module(id: int)-> dict:
    db = Session()
    result = db.query(ModuleModel).filter(ModuleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el módulo"})