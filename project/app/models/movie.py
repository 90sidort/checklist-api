from typing import List
from app.models.base import BaseClass
from enum import Enum

from sqlmodel import Field, Relationship

class MovieGenre(str, Enum):
    comedy = "Comedy"
    horror = "Horror"
    thriller = "Thriller"
    scifi = "SciFi"


class MovieBase(BaseClass):
    genre: MovieGenre
    reviews: List["Review"] = Relationship(back_populates="movie")


class Movie(MovieBase, table = True):
    id: int = Field(default=None, primary_key=True)


from app.models.review import Review


class MovieCreate(MovieBase):
    pass