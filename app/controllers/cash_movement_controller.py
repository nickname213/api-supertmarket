from pymongo.database import Database
from bson import ObjectId
from datetime import datetime
from app.models.cash_movement import CashMovement
from typing import List

class CashMovementController:
    def __init__(self, db: Database):
        self.col = db.get_collection("cash_movements")

    def create(self, data: CashMovement) -> CashMovement:
        doc = data.dict(by_alias=True)
        doc["date"] = datetime.utcnow()
        res = self.col.insert_one(doc)
        doc["_id"] = str(res.inserted_id)
        return CashMovement(**doc)

    def get_all(self) -> List[CashMovement]:
        cursor = self.col.find({})
        items = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            items.append(CashMovement(**doc))
        return items

    def get_by_id(self, id: str) -> CashMovement | None:
        doc = self.col.find_one({"_id": ObjectId(id)})
        if doc:
            doc["_id"] = str(doc["_id"])
            return CashMovement(**doc)
        return None

    def update(self, id: str, data: dict) -> CashMovement | None:
        self.col.update_one({"_id": ObjectId(id)}, {"$set": data})
        return self.get_by_id(id)

    def delete(self, id: str) -> bool:
        res = self.col.delete_one({"_id": ObjectId(id)})
        return res.deleted_count == 1
