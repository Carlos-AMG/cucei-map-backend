from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from schemas import GeoJSONModel
import models


router = APIRouter(
    prefix="/buildings",
    tags=["Buildings"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_buildings(data: GeoJSONModel, db: Session = Depends(get_db)):
    new_building = models.Building(**data.model_dump())
    db.add(new_building)
    db.commit()
    db.refresh(new_building)
    return new_building

@router.get("/{name}", status_code=status.HTTP_200_OK)
def retrieve_buildings(name: str, db: Session = Depends(get_db)):
    building = db.query(models.Building).filter(models.Building.name == name).first()
    
    if not building:
        raise HTTPException(status_code=404, detail=f'building with name: {name} not found')
    return building
