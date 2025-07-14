from fastapi import APIRouter, HTTPException, Depends
from app.models.product import Product, ProductCreate, ProductUpdate
from app.controllers.product_controller import ProductController
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from typing import List
from app.settings import settings
import httpx
from app.models.barcode_product import BarcodeProduct

router = APIRouter(prefix="/products", tags=["products"])

def get_db():
    client = MongoClient(settings.mongo_url, server_api=ServerApi('1'))
    return client[settings.mongo_db]

def get_controller(db=Depends(get_db)):
    return ProductController(db)

@router.post("/", response_model=Product)
def create_product(product: ProductCreate, controller: ProductController = Depends(get_controller)):
    return controller.create(product)

@router.get("/", response_model=List[Product])
def list_products(controller: ProductController = Depends(get_controller)):
    return controller.get_all()

@router.get("/{product_id}", response_model=Product)
def get_product(product_id: str, controller: ProductController = Depends(get_controller)):
    product = controller.get_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=Product)
def update_product(product_id: str, product: ProductUpdate, controller: ProductController = Depends(get_controller)):
    updated = controller.update(product_id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated

@router.delete("/{product_id}")
def delete_product(product_id: str, controller: ProductController = Depends(get_controller)):
    deleted = controller.delete(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"ok": True}

@router.get("/barcode/{barcode}", response_model=BarcodeProduct)
def get_product_by_barcode(barcode: str):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    try:
        response = httpx.get(url)
        data = response.json()
    except Exception as e:
        raise HTTPException(status_code=503, detail=f"Error consultando OpenFoodFacts: {str(e)}")
    if data.get("status") == 0:
        raise HTTPException(status_code=404, detail=f"Producto con código de barras {barcode} no encontrado en OpenFoodFacts.")
    return BarcodeProduct(
        code=barcode,
        product_name=data.get("product", {}).get("product_name"),
        brands=data.get("product", {}).get("brands"),
        quantity=data.get("product", {}).get("quantity"),
        image_url=data.get("product", {}).get("image_url"),
        status=data.get("status"),
        status_verbose=data.get("status_verbose"),
        product=data.get("product")
    ) 