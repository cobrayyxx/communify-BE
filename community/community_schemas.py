from typing import Union

from pydantic import BaseModel
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4

class Community(BaseModel):
    id: int = Field(None)
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=250)
    location:str = Field(..., max_length=200)
    schedule:str = Field(None)
    picture:str = Field(None)
    contact:str = Field(None)
    class Config:
        orm_mode = True