from pydantic import BaseModel, Field
# from bson import ObjectId
from datetime import datetime

class CashMovement(BaseModel):
    id: str = Field(..., alias="_id")
    type: str
    amount: int
    description: str
    date: datetime

    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class CashMovementCreate(BaseModel):
    type: str
    amount: int
    description: str
    date: datetime

class CashMovementUpdate(BaseModel):
    type: str | None = None
    amount: int | None = None
    description: str | None = None
    date: datetime | None = None
