from fastapi import APIRouter, HTTPException, Depends
from app.models.user import User, UserCreate, UserUpdate
from app.controllers.user_controller import UserController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List
from app.settings import settings

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    client = MongoClient(settings.mongo_url, server_api=ServerApi('1'))
    return client[settings.mongo_db]

def get_controller(db=Depends(get_db)):
    return UserController(db)

@router.post("/", response_model=User)
def create_user(user: UserCreate, controller: UserController = Depends(get_controller)):
    return controller.create(user)

@router.get("/", response_model=List[User])
def list_users(controller: UserController = Depends(get_controller)):
    return controller.get_all()

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str, controller: UserController = Depends(get_controller)):
    user = controller.get_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
def update_user(user_id: str, user: UserUpdate, controller: UserController = Depends(get_controller)):
    updated = controller.update(user_id, user)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/{user_id}")
def delete_user(user_id: str, controller: UserController = Depends(get_controller)):
    deleted = controller.delete(user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True} 