from pydantic import BaseModel, Field
from typing import Optional, List

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
                "username": "example_username",
                "name": "John",
                "last_name": "Doe",
                "user_type": "admin",
                "password": "example_password",
                "status": "active",
            }
        }