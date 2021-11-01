from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Task_Template, Task_TemplateCreate, Task, TaskCreate

app = FastAPI()

# @app.on_event("startup")
# async def on_startup():
#     await init_db()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/task_templates", response_model=list[Task_Template])
async def get_task_templates(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Task_Template))
    task_templates = result.scalars().all()
    return [Task_Template(name=task_template.name, risk=task_template.risk, description=task_template.description, id=task_template.id) for task_template in task_templates]


@app.post("/task_templates")
async def add_task_template(task_template: Task_TemplateCreate, session: AsyncSession = Depends(get_session)):
    task_template = Task_Template(name=task_template.name, risk=task_template.risk, description=task_template.description)
    session.add(task_template)
    await session.commit()
    await session.refresh(task_template)
    return task_template


@app.post("/tasks")
async def add_task(task: TaskCreate, session: AsyncSession = Depends(get_session)):
    task_template = await session.execute(select(Task_Template).where(Task_Template.id == task.task_template_id))
    if not task_template:
        raise HTTPException(status_code=404, detail="Task template not found")
    template = task_template.one()
    task = Task(task_template_id=1, task_template=template, done=False)
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task