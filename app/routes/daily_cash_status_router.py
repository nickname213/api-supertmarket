from fastapi import APIRouter, HTTPException, Depends
from app.models.daily_cash_status import DailyCashStatus, DailyCashStatusCreate, DailyCashStatusUpdate
from app.controllers.daily_cash_status_controller import DailyCashStatusController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List
from app.settings import settings

router = APIRouter(prefix="/daily-cash-status", tags=["daily-cash-status"])

def get_db():
    client = MongoClient(settings.mongo_url, server_api=ServerApi('1'))
    return client[settings.mongo_db]

def get_controller(db=Depends(get_db)):
    return DailyCashStatusController(db)

@router.post("/", response_model=DailyCashStatus)
def create_daily_cash_status(status: DailyCashStatusCreate, controller: DailyCashStatusController = Depends(get_controller)):
    return controller.create(status)

@router.get("/", response_model=List[DailyCashStatus])
def list_daily_cash_status(controller: DailyCashStatusController = Depends(get_controller)):
    return controller.get_all()

@router.get("/{status_id}", response_model=DailyCashStatus)
def get_daily_cash_status(status_id: str, controller: DailyCashStatusController = Depends(get_controller)):
    status = controller.get_by_id(status_id)
    if not status:
        raise HTTPException(status_code=404, detail="Daily cash status not found")
    return status

@router.put("/{status_id}", response_model=DailyCashStatus)
def update_daily_cash_status(status_id: str, status: DailyCashStatusUpdate, controller: DailyCashStatusController = Depends(get_controller)):
    updated = controller.update(status_id, status)
    if not updated:
        raise HTTPException(status_code=404, detail="Daily cash status not found")
    return updated

@router.delete("/{status_id}")
def delete_daily_cash_status(status_id: str, controller: DailyCashStatusController = Depends(get_controller)):
    deleted = controller.delete(status_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Daily cash status not found")
    return {"ok": True} 