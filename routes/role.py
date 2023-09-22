from fastapi import APIRouter
from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.role_database import Session, engine, Base
from jwt_manager import create_token, validate_token
from models.role_model import Role as RoleModel
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_bearer import JWTBearer
from schemas.role_scheme import Role

role_router = APIRouter()

Base.metadata.create_all(bind=engine)

@role_router.get('/roles', tags=['Role'], response_model=List[Role], status_code=200)
def get_roles() -> List[Role]:
    db = Session()
    result = db.query(RoleModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@role_router.post('/role', tags=['Role'], response_model=dict, status_code=201)
def create_role(role: Role) -> dict:
    db = Session()
    new_role = RoleModel(**role.dict())
    db.add(new_role)
    db.commit()
    return JSONResponse(status_code=201, content={"message": "The role has been created"})

@role_router.get('/role/{id}', tags=['Role'], response_model=Role)
def get_role(id: int = Path(ge=1, le=2000)) -> Role:
    db = Session()
    result = db.query(RoleModel).filter(RoleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@role_router.put('/role/{id}', tags=['Role'], response_model=dict, status_code=200)
def update_role(id: int, role: Role)-> dict:
    db = Session()
    result = db.query(RoleModel).filter(RoleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "not found"})
    result.role = role.role
    result.description = role.description
    db.commit()
    return JSONResponse(status_code=200, content={"message": "the role was successfully modified"})

@role_router.delete('/role/{id}', tags=['Role'], response_model=dict, status_code=200)
def delete_role(id: int)-> dict:
    db = Session()
    result = db.query(RoleModel).filter(RoleModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "the rol was successfully deleted"})