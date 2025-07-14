from fastapi import APIRouter, HTTPException, Depends
from app.models.client_account import ClientAccount, ClientAccountCreate, ClientAccountUpdate
from app.controllers.client_account_controller import ClientAccountController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List
from app.settings import settings

router = APIRouter(prefix="/client-accounts", tags=["client-accounts"])

def get_db():
    client = MongoClient(settings.mongo_url, server_api=ServerApi('1'))
    return client[settings.mongo_db]

def get_controller(db=Depends(get_db)):
    return ClientAccountController(db)

@router.post("/", response_model=ClientAccount)
def create_client_account(account: ClientAccountCreate, controller: ClientAccountController = Depends(get_controller)):
    return controller.create(account)

@router.get("/", response_model=List[ClientAccount])
def list_client_accounts(controller: ClientAccountController = Depends(get_controller)):
    return controller.get_all()

@router.get("/{account_id}", response_model=ClientAccount)
def get_client_account(account_id: str, controller: ClientAccountController = Depends(get_controller)):
    account = controller.get_by_id(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Client account not found")
    return account

@router.put("/{account_id}", response_model=ClientAccount)
def update_client_account(account_id: str, account: ClientAccountUpdate, controller: ClientAccountController = Depends(get_controller)):
    updated = controller.update(account_id, account)
    if not updated:
        raise HTTPException(status_code=404, detail="Client account not found")
    return updated

@router.delete("/{account_id}")
def delete_client_account(account_id: str, controller: ClientAccountController = Depends(get_controller)):
    deleted = controller.delete(account_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Client account not found")
    return {"ok": True} 