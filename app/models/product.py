from pydantic import BaseModel, Field
# from bson import ObjectId

class Product(BaseModel):
    id: str = Field(..., alias="_id")
    name: str
    barcode: str
    costPrice: int
    retailPrice: int
    currentStock: int
    unitType: str
    wholesalePrice: int
    wholesaleQuantity: int

    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class ProductCreate(BaseModel):
    name: str
    barcode: str
    costPrice: int
    retailPrice: int
    currentStock: int
    unitType: str
    wholesalePrice: int
    wholesaleQuantity: int

class ProductUpdate(BaseModel):
    name: str | None = None
    barcode: str | None = None
    costPrice: int | None = None
    retailPrice: int | None = None
    currentStock: int | None = None
    unitType: str | None = None
    wholesalePrice: int | None = None
    wholesaleQuantity: int | None = None
