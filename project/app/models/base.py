from sqlmodel import SQLModel

class BaseClass(SQLModel):
    title: str
    creator: str


class BaseModel(BaseClass):
    genre: str


class BaseResp(BaseModel):
    id: int