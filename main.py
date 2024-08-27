from fastapi import FastAPI
# from .routers import buildings
from database import engine
from routers import buildings, campuses
from config import settings
from fastapi.middleware.cors import CORSMiddleware
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(buildings.router)
app.include_router(campuses.router)
