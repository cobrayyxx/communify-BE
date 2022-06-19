from fastapi import Depends, FastAPI

from sub_app1 import users
from community import community_controller
import models
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(community_controller.router)
