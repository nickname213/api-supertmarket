from pydantic import BaseModel, Field
# from bson import ObjectId
from datetime import datetime
from typing import List, Dict, Any, Optional

class Sale(BaseModel):
    id: str = Field(..., alias="_id")
    date: datetime
    items: List[Dict[str, Any]]
    totalAmount: int
    paymentMethod: str
    amountPaid: int
    changeGiven: int
    recordedBy: Dict[str, Any]
    status: str
    totalRefundedAmount: int
    lastRefundDate: Optional[datetime] = None
    refundProcessedBy: Optional[Dict[str, Any]] = None

    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True
        # json_encoders = {ObjectId: str}

class SaleCreate(BaseModel):
    date: datetime
    items: List[Dict[str, Any]]
    totalAmount: int
    paymentMethod: str
    amountPaid: int
    changeGiven: int
    recordedBy: Dict[str, Any]
    status: str
    totalRefundedAmount: int
    lastRefundDate: Optional[datetime] = None
    refundProcessedBy: Optional[Dict[str, Any]] = None

class SaleUpdate(BaseModel):
    date: Optional[datetime] = None
    items: Optional[List[Dict[str, Any]]] = None
    totalAmount: Optional[int] = None
    paymentMethod: Optional[str] = None
    amountPaid: Optional[int] = None
    changeGiven: Optional[int] = None
    recordedBy: Optional[Dict[str, Any]] = None
    status: Optional[str] = None
    totalRefundedAmount: Optional[int] = None
    lastRefundDate: Optional[datetime] = None
    refundProcessedBy: Optional[Dict[str, Any]] = None