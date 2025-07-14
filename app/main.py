from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.settings import settings
import logging

print(f"[DEBUG] MongoDB URL: {settings.mongo_url}")

# Ping y listado de bases de datos y colecciones
try:
    client = MongoClient(settings.mongo_url, server_api=ServerApi('1'))
    # Ping
    client.admin.command('ping')
    print("[DEBUG] Pinged your deployment. You successfully connected to MongoDB with pymongo!")

    # Listar bases de datos
    dbs = client.list_database_names()
    print(f"[DEBUG] Bases de datos en el clúster: {dbs}")

    # Listar colecciones en la base de datos 'test'
    if 'test' in dbs:
        collections = client['test'].list_collection_names()
        print(f"[DEBUG] Colecciones en la base de datos 'test': {collections}")
    else:
        print("[DEBUG] La base de datos 'test' no existe en el clúster.")
except Exception as e:
    print(f"[DEBUG] pymongo connection error: {e}")

from app.routes.user_router import router as user_router
from app.routes.product_router import router as product_router
from app.routes.sale_router import router as sale_router
from app.routes.cash_movement_router import router as cash_movement_router
from app.routes.client_account_router import router as client_account_router
from app.routes.daily_cash_status_router import router as daily_cash_status_router
from app.routes.settings_router import router as settings_router

app = FastAPI(title="My FastAPI MVC App")

app.include_router(user_router)
app.include_router(product_router)
app.include_router(sale_router)
app.include_router(cash_movement_router)
app.include_router(client_account_router)
app.include_router(daily_cash_status_router)
app.include_router(settings_router)
