from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class BarcodeProduct(BaseModel):
    code: str
    product_name: Optional[str] = None
    brands: Optional[str] = None
    quantity: Optional[str] = None
    image_url: Optional[str] = Field(None, alias="image_url")
    status: Optional[int] = None
    status_verbose: Optional[str] = None
    product: Optional[Dict[str, Any]] = None  # Para exponer el objeto completo si se requiere 