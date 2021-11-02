from typing import List, Optional
from enum import Enum

from sqlmodel import SQLModel, Field, Relationship

class LevelEnum(str, Enum):
    begginer = "Begginer"
    advanced = "Advanced"
    experienced = "Experienced"
    expert = "Expert"


class UserCourseLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    course_id: Optional[int] = Field(
        default=None, foreign_key="course.id", primary_key=True
    )


class UserBase(SQLModel):
    name: str
    surname: str
    email: str
    courses_applied: List["Course"] = Relationship(back_populates="users", link_model=UserCourseLink)


class CourseBase(SQLModel):
    title: str
    date: str
    lecturer: str
    limit: int
    level: LevelEnum
    users_applied: List["User"] = Relationship(back_populates="courses", link_model=UserCourseLink)


class User(UserBase, table = True):
    id: int = Field(default=None, primary_key=True)


class Course(CourseBase, table = True):
    id: int = Field(default=None, primary_key=True)


class UserCreate(UserBase):
    pass


class CourseCreate(CourseBase):
    pass
