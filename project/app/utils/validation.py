from fastapi import HTTPException

from app.models.base import BaseModel

def validateCreation(input: BaseModel):
    if not input.title or len(input.title) < 3 or len(input.title) > 500:
        raise HTTPException(status_code=406, detail="Invalid title")
    if not input.creator or len(input.creator) < 3 or len(input.creator) > 500:
        raise HTTPException(status_code=406, detail="Invalid creator")