from pymongo.database import Database
from bson import ObjectId
from app.models.sale import Sale, SaleCreate, SaleUpdate
from typing import List

class SaleController:
    def __init__(self, db: Database):
        self.col = db.get_collection("sales")

    def create(self, data: SaleCreate) -> Sale:
        doc = data.dict()
        res = self.col.insert_one(doc)
        doc["_id"] = str(res.inserted_id)
        return Sale(**doc)

    def get_all(self) -> List[Sale]:
        cursor = self.col.find({})
        items = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            items.append(Sale(**doc))
        return items

    def get_by_id(self, id: str) -> Sale | None:
        doc = self.col.find_one({"_id": ObjectId(id)})
        if doc:
            doc["_id"] = str(doc["_id"])
            return Sale(**doc)
        return None

    def update(self, id: str, data: SaleUpdate) -> Sale | None:
        self.col.update_one({"_id": ObjectId(id)}, {"$set": data.dict(exclude_unset=True)})
        return self.get_by_id(id)

    def delete(self, id: str) -> bool:
        res = self.col.delete_one({"_id": ObjectId(id)})
        return res.deleted_count == 1 