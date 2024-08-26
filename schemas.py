from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Dict, Any


class GeoJSONModel(BaseModel):
    name: str
    geojson: Dict[str, Any]