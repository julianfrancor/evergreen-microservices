from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from routes.auth import auth_router
from routes.user import user_router
from routes.module import module_router
from routes.role import role_router

app = FastAPI()
app.title = "Evergreen"
app.version = "0.0.1"
app.port = 8001

app.add_middleware(ErrorHandler)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(module_router)
app.include_router(role_router)



@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')