from pydantic import BaseModel
from typing import Optional 

class TaskCreate(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    input:Optional[str] = None

class Task(BaseModel):
    id:int
    title:str
    description:Optional[str] = ""
    status:str = "pending"
