from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey, JSON
from sqlalchemy.orm import relationship
# from .database import Base
from database import Base

class Campus(Base):
    __tablename__ = "campuses"
    name = Column(String, primary_key=True, nullable=False)
    geojson = Column(JSON)
    # One-to-Many relationship with Building
    buildings = relationship("Building", back_populates="campus")

class Building(Base):
    __tablename__ = "buildings"
    name = Column(String, primary_key=True, nullable=False)
    geojson = Column(JSON)
    # Foreign key referencing the Campus
    campus_name = Column(String, ForeignKey("campuses.name"))
    # Relationship back to Campus
    campus = relationship("Campus", back_populates="buildings")