from fastapi import APIRouter, HTTPException, Depends
from app.models.cash_movement import CashMovement, CashMovementCreate, CashMovementUpdate
from app.controllers.cash_movement_controller import CashMovementController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List
from app.settings import settings

router = APIRouter(prefix="/cash-movements", tags=["cash-movements"])

def get_db():
    client = MongoClient(settings.mongo_url, server_api=ServerApi('1'))
    return client[settings.mongo_db]

def get_controller(db=Depends(get_db)):
    return CashMovementController(db)

@router.post("/", response_model=CashMovement)
def create_cash_movement(movement: CashMovementCreate, controller: CashMovementController = Depends(get_controller)):
    return controller.create(movement)

@router.get("/", response_model=List[CashMovement])
def list_cash_movements(controller: CashMovementController = Depends(get_controller)):
    return controller.get_all()

@router.get("/{movement_id}", response_model=CashMovement)
def get_cash_movement(movement_id: str, controller: CashMovementController = Depends(get_controller)):
    movement = controller.get_by_id(movement_id)
    if not movement:
        raise HTTPException(status_code=404, detail="Cash movement not found")
    return movement

@router.put("/{movement_id}", response_model=CashMovement)
def update_cash_movement(movement_id: str, movement: CashMovementUpdate, controller: CashMovementController = Depends(get_controller)):
    updated = controller.update(movement_id, movement.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Cash movement not found")
    return updated

@router.delete("/{movement_id}")
def delete_cash_movement(movement_id: str, controller: CashMovementController = Depends(get_controller)):
    deleted = controller.delete(movement_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cash movement not found")
    return {"ok": True} 