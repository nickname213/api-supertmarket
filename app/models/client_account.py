from pydantic import BaseModel, Field
# from bson import ObjectId

class ClientAccount(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    currentDebt: int

    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class ClientAccountCreate(BaseModel):
    name: str
    currentDebt: int

class ClientAccountUpdate(BaseModel):
    name: str | None = None
    currentDebt: int | None = None
