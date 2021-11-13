from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

class ReviewBase(SQLModel):
    text: Optional[str]
    rating: int

    book_id: Optional[int] = Field(default=None, foreign_key="book.id")
    book: Optional["Book"] = Relationship(back_populates="reviews")
    album_id: Optional[int] = Field(default=None, foreign_key="album.id")
    album: Optional["Album"] = Relationship(back_populates="album")
    movie_id: Optional[int] = Field(default=None, foreign_key="movie.id")
    movie: Optional["Movie"] = Relationship(back_populates="movie")


class Review(ReviewBase, table = True):
    id: int = Field(default=None, primary_key=True)


from app.models.book import Book
from app.models.album import Album
from app.models.movie import Movie


class ReviewCreate(ReviewBase):
    pass