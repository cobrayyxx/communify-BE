from typing import Union

from pydantic import BaseModel
from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from comment.comment_schemas import Comment
import json
class Community(BaseModel):
    id: int = Field(None)
    name: str = Field(..., max_length=100)
    description: str = Field(..., max_length=250)
    location:str = Field(..., max_length=200)
    schedule:str = Field(None)
    picture:str = Field(None)
    contact:str = Field(None)
    comments:list[Comment] = []
    
    # @classmethod
    # def __get_validators__(cls):
    #     yield cls.validate_to_json

    # @classmethod
    # def validate_to_json(cls, value):
    #     if isinstance(value, str):
    #         return cls(**json.loads(value))
    #     return value
    

    class Config:
        orm_mode = True