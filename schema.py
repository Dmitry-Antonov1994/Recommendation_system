from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from database import Base


class Post(Base):
    __tablename__ = 'post'
    __table_args__ = {'schema': 'public'}
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)


class PostGet(BaseModel):
    id: int
    text: str
    topic: str

    class Config:
        orm_mode = True


class Response(BaseModel):
    exp_group: str
    recommendations: List[PostGet]
