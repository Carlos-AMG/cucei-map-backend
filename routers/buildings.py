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
    existing_building = db.query(models.Building).filter_by(name=data.name).first()
    
    if existing_building:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Building already exists."
        )
    
    new_building = models.Building(**data.model_dump())
    db.add(new_building)
    db.commit()
    db.refresh(new_building)
    return new_building

@router.get("/", status_code=status.HTTP_200_OK)
def retrieve_all_buildings(db: Session = Depends(get_db)):
    return db.query(models.Building).all()


@router.get("/{name}", status_code=status.HTTP_200_OK)
def retrieve_buildings(name: str, db: Session = Depends(get_db)):
    building = db.query(models.Building).filter(models.Building.name == name).first()
    if not building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Building with name: {name} not found')
    return building
