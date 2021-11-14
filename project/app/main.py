from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models.book import Book
from app.models.movie import Movie
from app.models.album import Album
from app.models.base import BaseModel, BaseResp
from app.models.review import Review, ReviewCreate
from app.utils.validation import validateCreation, validateReview
from app.utils.updatePar import updateParameters, updateReview

app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.post("/review")
async def add_review(type: str, data: ReviewCreate, session: AsyncSession = Depends(get_session)):
    validateReview(data)
    try:
        if type == "book":
            review = Review(text=data.text, rating=data.rating, book_id=data.book_id)
        elif (type == "movie"):
            review = Review(text=data.text, rating=data.rating, movie_id=data.movie_id)
        else:
            review = Review(text=data.text, rating=data.rating, album_id=data.album_id)
        session.add(review)
        await session.commit()
        await session.refresh(review)
        return review
    except:
        raise HTTPException(status_code=400, detail=f"Failed to add review!")

@app.get("/review")
async def get_review(id: int, session: AsyncSession = Depends(get_session)):
    try:
        review = await session.get(Review, id)
        if not review:
            raise HTTPException(status_code=404, detail=f"Review not found!")
        if review.book_id:
            object = await session.get(Book, review.book_id)
        elif review.movie_id:
            object = await session.get(Movie, review.movie_id)
        else:
            object = await session.get(Album, review.album_id)
        if not object:
            raise HTTPException(status_code=404, detail=f"Review object invalid!")
        response = {}
        response["review"] = review
        response["object"] = object
        return response
    except:
        raise HTTPException(status_code=400, detail=f"Failed to get review!")

@app.put("/review", response_model=Review)
async def get_review(id: int, data: ReviewCreate ,session: AsyncSession = Depends(get_session)):
    validateReview(data)
    try:
        review = await session.get(Review, id)
        if not review:
            raise HTTPException(status_code=404, detail=f"Review not found!")
        response = updateReview(review, data)
        session.add(response)
        await session.commit()
        await session.refresh(response)
        return response
    except:
        raise HTTPException(status_code=400, detail=f"Failed to update review!")


@app.delete("/review", response_model= bool)
async def delete_hero(id: int, session: AsyncSession = Depends(get_session)):
    result = await session.get(Review, id)
    if not result:
        raise HTTPException(status_code=404, detail=f"{type} not found!")
    await session.delete(result)
    await session.commit()
    return True


@app.post("/add")
async def add(type: str, data: BaseModel, session: AsyncSession = Depends(get_session)):
    validateCreation(data)
    if (type == "book"):
        entry = Book(title=data.title, creator=data.creator, genre=data.genre)
    elif (type == "movie"):
        entry = Movie(title=data.title, creator=data.creator, genre=data.genre)
    else:
        entry = Album(title=data.title, creator=data.creator, genre=data.genre)
    if not entry.genre:
        raise HTTPException(status_code=404, detail="Invalid genre!")
    session.add(entry)
    await session.commit()
    await session.refresh(entry)
    return entry


@app.get("/get", response_model=list[BaseResp])
async def getData(type: str, session: AsyncSession = Depends(get_session)):
    if (type == "book"):
        repo = Book
    elif (type == "movie"):
        repo = Movie
    else:
        repo = Album
    results = await session.execute(select(repo))
    objects = results.scalars().all()
    print(888, objects)
    return [repo(id=object.id, title=object.title, creator=object.creator, genre=object.genre) for object in objects]


@app.put("/update", response_model=BaseResp)
async def update(type: str, id: int, data: BaseModel, session: AsyncSession = Depends(get_session)):
    validateCreation(data)
    if (type == "book"):
        repo = Book
    elif (type == "movie"):
        repo = Movie
    else:
        repo = Album
    result = await session.get(repo, id)
    if not result:
        raise HTTPException(status_code=404, detail=f"{type} not found!")
    updateParameters(result, data)
    session.add(result)
    await session.commit()
    await session.refresh(result)
    return result

@app.delete("/delete", response_model= bool)
async def delete_hero(type: str, id: int, session: AsyncSession = Depends(get_session)):
    if (type == "book"):
        repo = Book
    elif (type == "movie"):
        repo = Movie
    else:
        repo = Album
    result = await session.get(repo, id)
    if not result:
        raise HTTPException(status_code=404, detail=f"{type} not found!")
    await session.delete(result)
    await session.commit()
    return True