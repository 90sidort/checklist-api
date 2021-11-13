from app.models.base import BaseClass
from enum import Enum

from sqlmodel import Field

class BookGenre(str, Enum):
    scifi = "SciFi"
    classics = "Classics"
    romance = "Romance"
    fantasy = "Fantasy"


class BookBase(BaseClass):
    genre: BookGenre


class Book(BookBase, table = True):
    id: int = Field(default=None, primary_key=True)


class BookCreate(BookBase):
    pass