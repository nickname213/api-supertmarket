from fastapi import APIRouter, HTTPException, Depends
from app.models.settings import Settings, SettingsCreate, SettingsUpdate
from app.controllers.settings_controller import SettingsController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List
from app.settings import settings

router = APIRouter(prefix="/settings", tags=["settings"])

def get_db():
    client = MongoClient(settings.mongo_url, server_api=ServerApi('1'))
    return client[settings.mongo_db]

def get_controller(db=Depends(get_db)):
    return SettingsController(db)

@router.post("/", response_model=Settings)
def create_settings(settings_data: SettingsCreate, controller: SettingsController = Depends(get_controller)):
    return controller.create(settings_data)

@router.get("/", response_model=List[Settings])
def list_settings(controller: SettingsController = Depends(get_controller)):
    return controller.get_all()

@router.get("/{settings_id}", response_model=Settings)
def get_settings(settings_id: str, controller: SettingsController = Depends(get_controller)):
    settings_obj = controller.get_by_id(settings_id)
    if not settings_obj:
        raise HTTPException(status_code=404, detail="Settings not found")
    return settings_obj

@router.put("/{settings_id}", response_model=Settings)
def update_settings(settings_id: str, settings_data: SettingsUpdate, controller: SettingsController = Depends(get_controller)):
    updated = controller.update(settings_id, settings_data)
    if not updated:
        raise HTTPException(status_code=404, detail="Settings not found")
    return updated

@router.delete("/{settings_id}")
def delete_settings(settings_id: str, controller: SettingsController = Depends(get_controller)):
    deleted = controller.delete(settings_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Settings not found")
    return {"ok": True} 