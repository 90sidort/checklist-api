from typing import List, Optional
from enum import Enum

from sqlmodel import SQLModel, Field, Relationship

class RiskEnum(str, Enum):
    low = "Low"
    normal = "Normal"
    high = "High"
    extreme = "Extreme"

    
class Task_TemplateBase(SQLModel):
    name: str
    risk: RiskEnum
    description: Optional[str] = None
    tasks: List["Task"] = Relationship(back_populates="task_templates")


class Task_Template(Task_TemplateBase, table = True):
    id: int = Field(default=None, primary_key=True)


class TaskBase(SQLModel):
    task_template_id: int = Field(default=None, foreign_key="task_template.id")
    task_template: Task_Template = Relationship(back_populates="tasks")
    checklist_template_id: Optional[int] = Field(default=None, foreign_key="checklist_template.id")
    checklist_template: Optional["Task_Template"] = Relationship(back_populates="tasks")
    done: bool


class Task(TaskBase, table = True):
    id: int = Field(default=None, primary_key=True)


class Checklist_TemplateBase(SQLModel):
    name: str
    tasks: List[Task] = Relationship(back_populates="checklist_templates")
    checklists: List["Checklist"] = Relationship(back_populates="checklist_templates")


class Checklist_Template(Checklist_TemplateBase, table = True):
    id: int = Field(default=None, primary_key=True)


class ChecklistBase(SQLModel):
    name: str
    date: str
    checklist_template_id: int = Field(default=None, foreign_key="checklist_template.id")
    checklist_template: "Task_Template" = Relationship(back_populates="checklists")


class Checklist(ChecklistBase, table = True):
    id: int = Field(default=None, primary_key=True)


class Task_TemplateCreate(Task_TemplateBase):
    pass


class TaskCreate(TaskBase):
    pass

# TaskTemplate - id, name, description (optional), risk
# Task - id, TaskTemplate, done
# ChecklistTemplate - id, name, tasks (list of tasks)
# Checklist - id, date, ChecklistTemplate