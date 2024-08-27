from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func
from database import get_db
from schemas import CampusModel
import models


router = APIRouter(
    prefix="/campuses",
    tags=["Campuses"]
)


# Endpoint to create a new campus
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_campuses(data: CampusModel, db: Session = Depends(get_db)):  
    existing_campus = db.query(models.Campus).filter_by(name=data.name).first()

    if existing_campus:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Campus already exists"
        )
    
    new_campus = models.Campus(**data.dict())
    db.add(new_campus)
    db.commit()
    db.refresh(new_campus)
    return new_campus

# Endpoint to retrieve all campuses
@router.get("/", status_code=status.HTTP_200_OK)
def retrieve_all_campuses(db: Session = Depends(get_db)):
    return db.query(models.Campus).all()

# Endpoint to retrieve a specific campus by name
@router.get("/{name}", status_code=status.HTTP_200_OK)
def retrieve_campus_by_name(name: str, db: Session = Depends(get_db)):
    # campus = db.query(models.Campus).filter(models.Campus.name == name).first()  
    campus = db.query(models.Campus).options(joinedload(models.Campus.buildings)).filter(models.Campus.name == name).first()
    if not campus:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Campus with name '{name}' not found")
    return campus