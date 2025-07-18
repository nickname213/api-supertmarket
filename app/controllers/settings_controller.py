from pymongo.database import Database
from bson import ObjectId
from app.models.settings import Settings, SettingsCreate, SettingsUpdate
from typing import List

class SettingsController:
    def __init__(self, db: Database):
        self.col = db.get_collection("settings")

    def create(self, data: SettingsCreate) -> Settings:
        doc = data.dict()
        res = self.col.insert_one(doc)
        doc["_id"] = str(res.inserted_id)
        return Settings(**doc)

    def get_all(self) -> List[Settings]:
        cursor = self.col.find({})
        items = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            items.append(Settings(**doc))
        return items

    def get_by_id(self, id: str) -> Settings | None:
        doc = self.col.find_one({"_id": ObjectId(id)})
        if doc:
            doc["_id"] = str(doc["_id"])
            return Settings(**doc)
        return None

    def update(self, id: str, data: SettingsUpdate) -> Settings | None:
        self.col.update_one({"_id": ObjectId(id)}, {"$set": data.dict(exclude_unset=True)})
        return self.get_by_id(id)

    def delete(self, id: str) -> bool:
        res = self.col.delete_one({"_id": ObjectId(id)})
        return res.deleted_count == 1 