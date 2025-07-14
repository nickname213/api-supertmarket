from pymongo.database import Database
from bson import ObjectId
from app.models.product import Product, ProductCreate, ProductUpdate
from typing import List

class ProductController:
    def __init__(self, db: Database):
        self.col = db.get_collection("products")

    def create(self, data: ProductCreate) -> Product:
        doc = data.dict()
        res = self.col.insert_one(doc)
        doc["_id"] = str(res.inserted_id)
        return Product(**doc)

    def get_all(self) -> List[Product]:
        cursor = self.col.find({})
        items = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            items.append(Product(**doc))
        return items

    def get_by_id(self, id: str) -> Product | None:
        doc = self.col.find_one({"_id": ObjectId(id)})
        if doc:
            doc["_id"] = str(doc["_id"])
            return Product(**doc)
        return None

    def update(self, id: str, data: ProductUpdate) -> Product | None:
        self.col.update_one({"_id": ObjectId(id)}, {"$set": data.dict(exclude_unset=True)})
        return self.get_by_id(id)

    def delete(self, id: str) -> bool:
        res = self.col.delete_one({"_id": ObjectId(id)})
        return res.deleted_count == 1 