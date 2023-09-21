from fastapi import Depends, FastAPI, Body, HTTPException, Path, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler
from routes.auth import auth_router
from routes.user import user_router

app = FastAPI()
app.title = "Evergreen"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(user_router)
app.include_router(auth_router)



@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')