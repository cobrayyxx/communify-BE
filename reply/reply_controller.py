from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from . import reply_schemas,reply_repo
import models
from database import SessionLocal, engine, get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["reply"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/reply/", response_model= reply_schemas.Reply)
def create_reply_controller(
    reply: reply_schemas.Reply, db: Session = Depends(get_db)
):
    return reply_repo.create_reply(db=db, reply=reply)


@router.get("/reply/", response_model=list[reply_schemas.Reply])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    replies = reply_repo.get_reply(db, skip=skip, limit=limit)
    return replies