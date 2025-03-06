from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SensorData(BaseModel):
    temperature: float
    timestamp: Optional[datetime] = None  
