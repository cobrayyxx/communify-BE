from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

from . import community_repo, community_schemas
import models
from database import SessionLocal, engine, get_db

router = APIRouter(
    prefix="/api/v1",
    tags=["community"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/community/", response_model=community_schemas.Community)
def create_community_controller(
    community: community_schemas.Community, db: Session = Depends(get_db)
):
    return community_repo.create_community(db=db, community=community)



@router.get("/community/", response_model=list[community_schemas.Community])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    communities = community_repo.get_community(db, skip=skip, limit=limit)
    return communities

