from pymongo.database import Database
from bson import ObjectId
from app.models.client_account import ClientAccount, ClientAccountCreate, ClientAccountUpdate
from typing import List

class ClientAccountController:
    def __init__(self, db: Database):
        self.col = db.get_collection("client_accounts")

    def create(self, data: ClientAccountCreate) -> ClientAccount:
        doc = data.dict()
        res = self.col.insert_one(doc)
        doc["_id"] = str(res.inserted_id)
        return ClientAccount(**doc)

    def get_all(self) -> List[ClientAccount]:
        cursor = self.col.find({})
        items = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            items.append(ClientAccount(**doc))
        return items

    def get_by_id(self, id: str) -> ClientAccount | None:
        doc = self.col.find_one({"_id": ObjectId(id)})
        if doc:
            doc["_id"] = str(doc["_id"])
            return ClientAccount(**doc)
        return None

    def update(self, id: str, data: ClientAccountUpdate) -> ClientAccount | None:
        self.col.update_one({"_id": ObjectId(id)}, {"$set": data.dict(exclude_unset=True)})
        return self.get_by_id(id)

    def delete(self, id: str) -> bool:
        res = self.col.delete_one({"_id": ObjectId(id)})
        return res.deleted_count == 1 