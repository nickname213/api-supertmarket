from pydantic import BaseModel, Field, EmailStr
# from bson import ObjectId

class User(BaseModel):
    id: str = Field(..., alias="_id")
    username: str
    password: str
    role: str
    email: EmailStr
    simplifiedMode: bool

    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class UserCreate(BaseModel):
    username: str
    password: str
    role: str
    email: EmailStr
    simplifiedMode: bool

class UserUpdate(BaseModel):
    username: str | None = None
    password: str | None = None
    role: str | None = None
    email: EmailStr | None = None
    simplifiedMode: bool | None = None
