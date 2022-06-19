from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, get_db
from . import  community_schemas
import models



def get_community(db: Session= Depends(get_db), skip: int = 0, limit: int = 100):
    return db.query(models.Community).offset(skip).limit(limit).all()

def create_community(db: Session, community: community_schemas.Community):
    db_item = models.Community(**community.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item 

def get_community_by_id(db: Session, community_id: int):
    return db.query(models.Community).filter(models.Community.id == int(community_id)).first()