from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from . import  community_schemas
import models



def get_community(db: Session= Depends(get_db), skip: int = 0, limit: int = 100):
    return db.query(models.Community).offset(skip).limit(limit).all()

def create_community(db: Session, community: community_schemas.Community):
    db_community = models.Community(**community.dict())
    db.add(db_community)
    db.commit()
    db.refresh(db_community)
    return db_community