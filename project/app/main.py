from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Task, TaskCreate

app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/tasks", response_model=list[Task])
async def get_tasks(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task))
    tasks = result.scalars().all()
    return [Task(name=task.name, risk=task.risk, done=task.done, description=task.description, id=task.id) for task in tasks]


@app.post("/tasks")
async def add_song(task: TaskCreate, session: AsyncSession = Depends(get_session)):
    task = Task(name=task.name, risk=task.risk, done=task.done, description=task.description)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task
