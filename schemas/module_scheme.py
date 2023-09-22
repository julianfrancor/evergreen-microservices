from pydantic import BaseModel, Field
from typing import Optional, List


class Module(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=5, max_length=15)
    description: str = Field(min_length=3, max_length=50)
    module_type: str = Field(min_length=3, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Module_test",
                "description": "Descripción del modulo",
                "module_type": "Finance"
            }
        }
