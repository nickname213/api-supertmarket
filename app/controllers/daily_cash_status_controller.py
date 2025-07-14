from pymongo.database import Database
from bson import ObjectId
from app.models.daily_cash_status import DailyCashStatus, DailyCashStatusCreate, DailyCashStatusUpdate
from typing import List

class DailyCashStatusController:
    def __init__(self, db: Database):
        self.col = db.get_collection("daily_cash_status")

    def create(self, data: DailyCashStatusCreate) -> DailyCashStatus:
        doc = data.dict()
        res = self.col.insert_one(doc)
        doc["_id"] = str(res.inserted_id)
        return DailyCashStatus(**doc)

    def get_all(self) -> List[DailyCashStatus]:
        cursor = self.col.find({})
        items = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            items.append(DailyCashStatus(**doc))
        return items

    def get_by_id(self, id: str) -> DailyCashStatus | None:
        doc = self.col.find_one({"_id": ObjectId(id)})
        if doc:
            doc["_id"] = str(doc["_id"])
            return DailyCashStatus(**doc)
        return None

    def update(self, id: str, data: DailyCashStatusUpdate) -> DailyCashStatus | None:
        self.col.update_one({"_id": ObjectId(id)}, {"$set": data.dict(exclude_unset=True)})
        return self.get_by_id(id)

    def delete(self, id: str) -> bool:
        res = self.col.delete_one({"_id": ObjectId(id)})
        return res.deleted_count == 1 