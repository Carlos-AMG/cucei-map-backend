from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text, ForeignKey, JSON
# from .database import Base
from database import Base

class Building(Base):
    __tablename__ = "buildings"
    name = Column(String, primary_key=True, nullable=False)
    geojson = Column(JSON)