from typing import List, Optional
from enum import Enum

from sqlmodel import SQLModel, Field, Relationship

class RiskEnum(str, Enum):
    low = "Low"
    normal = "Normal"
    high = "High"
    extreme = "Extreme"


class TaskChecklistLink(SQLModel, table=True):
    task_id: Optional[int] = Field(
        default=None, foreign_key="task.id", primary_key=True
    )
    checklist_id: Optional[int] = Field(
        default=None, foreign_key="checklist.id", primary_key=True
    )

    
class TaskBase(SQLModel):
    name: str
    risk: RiskEnum
    done: bool
    description: Optional[str] = None
    checklists: List["Checklist"] = Relationship(back_populates="tasks", link_model=TaskChecklistLink)


class Task(TaskBase, table = True):
    id: int = Field(default=None, primary_key=True)


class ChecklistBase(SQLModel):
    name: str
    date: str
    tasks: List[Task] = Relationship(back_populates="checklists", link_model=TaskChecklistLink)


class Checklist(ChecklistBase, table = True):
    id: int = Field(default=None, primary_key=True)


class TaskCreate(TaskBase):
    pass
