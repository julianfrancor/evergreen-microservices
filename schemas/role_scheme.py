from pydantic import BaseModel, Field
from typing import Optional, List

class Role(BaseModel):
    id: Optional[int] = None
    role: str = Field(min_length=5, max_length=15)
    description: str = Field(min_length=3, max_length=50)


    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "role": "Role name",
                "description": "Role description"
            }
        }