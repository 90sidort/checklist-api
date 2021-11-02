from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Course, User, UserCreate, CourseCreate

app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/course", response_model=list[Course])
async def get_courses(session: AsyncSession = Depends(get_session)):
    results = await session.execute(select(Course))
    courses = results.scalars().all()
    return [Course(title=course.title, date=course.date, lecturer=course.lecturer,
    limit=course.limit, level=course.level, id=course.id) for course in courses]


@app.post("/course")
async def add_course(course: CourseCreate, session: AsyncSession = Depends(get_session)):
    course = Course(title=course.title, date=course.date, lecturer=course.lecturer,
    limit=course.limit, level=course.level)
    session.add(course)
    await session.commit()
    await session.refresh(course)
    return course


