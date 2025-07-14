from pydantic import BaseModel, Field
# from bson import ObjectId

class Settings(BaseModel):
    id: str = Field(..., alias="_id")
    businessName: str
    receiptHeaderText: str
    logoIconName: str
    logoIconColor: str

    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class SettingsCreate(BaseModel):
    businessName: str
    receiptHeaderText: str
    logoIconName: str
    logoIconColor: str

class SettingsUpdate(BaseModel):
    businessName: str | None = None
    receiptHeaderText: str | None = None
    logoIconName: str | None = None
    logoIconColor: str | None = None