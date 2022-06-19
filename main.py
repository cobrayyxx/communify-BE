from fastapi import Depends, FastAPI

from user import user_controller
from community import community_controller
from comment import comment_controller
from reply import reply_controller
import models
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user_controller.router)
app.include_router(community_controller.router)
app.include_router(comment_controller.router)
app.include_router(reply_controller.router)
