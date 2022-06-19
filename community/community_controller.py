from fastapi import Depends, FastAPI, HTTPException, APIRouter, UploadFile, File
from sqlalchemy.orm import Session

from . import community_repo, community_schemas
import models
from database import SessionLocal, engine, get_db
import cloudinary
import cloudinary.uploader
from fastapi.encoders import jsonable_encoder
from typing import Optional

router = APIRouter(
    prefix="/api/v1",
    tags=["community"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/community/", response_model=community_schemas.Community)
def create_community_controller(
    community: community_schemas.Community, db: Session = Depends(get_db), file:Optional[UploadFile] = File(None)
):
    print(file)
    result = cloudinary.uploader.upload(file.file, folder = 'waffle-hack-communify')
    url = result.get('secure_url')
    community = jsonable_encoder(community)
    community['picture'] = url
    print(community)
    print(url)
    return community_repo.create_community(db=db, community=community)



@router.get("/community/", response_model=list[community_schemas.Community])
def read_communities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    communities = community_repo.get_community(db, skip=skip, limit=limit)
    return communities

@router.get("/community/{community_id}",response_model=community_schemas.Community)
def read_certain_community(community_id: int,db: Session = Depends(get_db)):
    community = community_repo.get_community_by_id(db, community_id)
    return community
