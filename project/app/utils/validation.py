from fastapi import HTTPException

from app.models.base import BaseModel
from app.models.review import ReviewBase

def validateCreation(input: BaseModel):
    if not input.title or len(input.title) < 3 or len(input.title) > 500:
        raise HTTPException(status_code=406, detail="Invalid title")
    if not input.creator or len(input.creator) < 3 or len(input.creator) > 500:
        raise HTTPException(status_code=406, detail="Invalid creator")

def validateReview(input: ReviewBase):
    if input.text:
        if not input.text or len(input.text) < 3 or len(input.text) > 2000:
            raise HTTPException(status_code=406, detail="Invalid review text")
    if not input.rating:
        raise HTTPException(status_code=406, detail="Missing review score")
    if not isinstance(input.rating, int):
        raise HTTPException(status_code=406, detail="Review should be an integer")
    if input.rating > 10 or input.rating < 0:
        raise HTTPException(status_code=406, detail="Review should be between 0 and 10")