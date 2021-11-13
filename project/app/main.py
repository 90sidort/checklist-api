from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models.book import Book
from app.models.movie import Movie
from app.models.album import Album
from app.models.base import BaseModel, BaseResp
from app.utils.validation import validateCreation

app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


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
    return [repo(id=object.id, title=object.title, creator=object.creator, genre=object.genre) for object in objects]
