from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from . import  comment_schemas
import models



def get_comment(db: Session= Depends(get_db), skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()

def create_comment(db: Session, comment: comment_schemas.Comment):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment