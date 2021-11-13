from typing import List, Optional
from app.models.base import BaseClass
from enum import Enum
from sqlmodel import Field, Relationship

class BookGenre(str, Enum):
    scifi = "SciFi"
    classics = "Classics"
    romance = "Romance"
    fantasy = "Fantasy"


class BookBase(BaseClass):
    genre: BookGenre
    reviews: List["Review"] = Relationship(back_populates="book")


class Book(BookBase, table = True):
    id: int = Field(default=None, primary_key=True)


from app.models.review import Review


class BookCreate(BookBase):
    pass