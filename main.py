from fastapi import FastAPI
# from .routers import buildings
from database import engine
from routers import buildings
from config import settings
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.include_router(buildings.router)
