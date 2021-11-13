from typing import List
from app.models.base import BaseClass
from enum import Enum

from sqlmodel import Field, Relationship

class AlbumGenre(str, Enum):
    pop = "Pop"
    classical = "Classical"
    hiphop = "HipHop"
    rock = "Rock"


class AlbumBase(BaseClass):
    genre: AlbumGenre
    reviews: List["Review"] = Relationship(back_populates="album")


class Album(AlbumBase, table = True):
    id: int = Field(default=None, primary_key=True)


from app.models.review import Review


class AlbumCreate(AlbumBase):
    pass