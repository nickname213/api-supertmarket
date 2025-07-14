from fastapi import APIRouter, HTTPException, Depends
from app.models.sale import Sale, SaleCreate, SaleUpdate
from app.controllers.sale_controller import SaleController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List
from app.settings import settings

router = APIRouter(prefix="/sales", tags=["sales"])

def get_db():
    client = MongoClient(settings.mongo_url, server_api=ServerApi('1'))
    return client[settings.mongo_db]

def get_controller(db=Depends(get_db)):
    return SaleController(db)

@router.post("/", response_model=Sale)
def create_sale(sale: SaleCreate, controller: SaleController = Depends(get_controller)):
    return controller.create(sale)

@router.get("/", response_model=List[Sale])
def list_sales(controller: SaleController = Depends(get_controller)):
    return controller.get_all()

@router.get("/{sale_id}", response_model=Sale)
def get_sale(sale_id: str, controller: SaleController = Depends(get_controller)):
    sale = controller.get_by_id(sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@router.put("/{sale_id}", response_model=Sale)
def update_sale(sale_id: str, sale: SaleUpdate, controller: SaleController = Depends(get_controller)):
    updated = controller.update(sale_id, sale)
    if not updated:
        raise HTTPException(status_code=404, detail="Sale not found")
    return updated

@router.delete("/{sale_id}")
def delete_sale(sale_id: str, controller: SaleController = Depends(get_controller)):
    deleted = controller.delete(sale_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Sale not found")
    return {"ok": True} 