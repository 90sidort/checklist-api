from app.models.base import BaseClass
from enum import Enum

from sqlmodel import Field

class MovieGenre(str, Enum):
    comedy = "Comedy"
    horror = "Horror"
    thriller = "Thriller"
    scifi = "SciFi"


class MovieBase(BaseClass):
    genre: MovieGenre


class Movie(MovieBase, table = True):
    id: int = Field(default=None, primary_key=True)


class MovieCreate(MovieBase):
    pass