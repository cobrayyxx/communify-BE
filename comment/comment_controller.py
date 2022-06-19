from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from community import community_schemas

from . import comment_schemas,comment_repo
import models
from database import SessionLocal, engine, get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["comment"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/comment/", response_model= comment_schemas.Comment)
def create_comment_controller(
    comment: comment_schemas.Comment, db: Session = Depends(get_db)
):
    return comment_repo.create_comment(db=db, comment=comment)


@router.get("/comment/", response_model=list[comment_schemas.Comment])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = comment_repo.get_comment(db, skip=skip, limit=limit)
    return comments