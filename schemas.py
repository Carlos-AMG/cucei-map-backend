from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Dict, Any


class GeoJSONModel(BaseModel):
    name: str
    campus_name: str
    geojson: Dict[str, Any]

class CampusModel(BaseModel):
    name: str
    geojson: Dict[str, Any]