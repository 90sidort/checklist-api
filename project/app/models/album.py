from app.models.base import BaseClass
from enum import Enum

from sqlmodel import Field

class AlbumGenre(str, Enum):
    pop = "Pop"
    classical = "Classical"
    hiphop = "HipHop"
    rock = "Rock"


class AlbumBase(BaseClass):
    genre: AlbumGenre


class Album(AlbumBase, table = True):
    id: int = Field(default=None, primary_key=True)


class AlbumCreate(AlbumBase):
    pass