from pydantic import BaseModel
from typing import List

class TestSchema(BaseModel):
    name:str
    class Config:
        orm_mode = True

class PostTestSchema(TestSchema):
    coordinates:List[List[float]]