from pydantic import BaseModel, Field
# from bson import ObjectId
from datetime import datetime

class DailyCashStatus(BaseModel):
    id: str = Field(..., alias="_id")
    startingCash: int
    date: datetime
    isOpen: bool

    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class DailyCashStatusCreate(BaseModel):
    startingCash: int
    date: datetime
    isOpen: bool

class DailyCashStatusUpdate(BaseModel):
    startingCash: int | None = None
    date: datetime | None = None
    isOpen: bool | None = None
