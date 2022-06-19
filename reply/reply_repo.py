from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from . import  reply_schemas
import models



def get_reply(db: Session= Depends(get_db), skip: int = 0, limit: int = 100):
    return db.query(models.Reply).offset(skip).limit(limit).all()

def create_reply(db: Session, reply: reply_schemas.Reply):
    db_reply = models.Reply(**reply.dict())
    db.add(db_reply)
    db.commit()
    db.refresh(db_reply)
    return db_reply