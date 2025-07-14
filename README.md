# API SuperTmarket

API de supermercado construida con FastAPI, MongoDB y Docker.

## Características

- CRUD para usuarios, productos, ventas, movimientos de caja, cuentas de cliente, estados de caja diaria y configuraciones.
- Consulta de productos por código de barras usando la API pública de OpenFoodFacts.
- Conexión flexible a MongoDB local, en Docker o en la nube (Atlas).

---

## Requisitos

- Docker y Docker Compose (recomendado para desarrollo y pruebas)
- Python 3.10+ (si corres localmente)

---

## Configuración de variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (ajusta según tu entorno):

### Para MongoDB local o Docker:

```
MONGO_USER=root
MONGO_PASSWORD=examplepassword
MONGO_HOST=mongo
MONGO_DB=supertmarket
MONGO_PROTOCOL=mongodb
```

### Para MongoDB Atlas (nube):

```
MONGO_USER=tu_usuario
MONGO_PASSWORD=tu_contraseña
MONGO_HOST=clouster.mnoc96q.mongodb.net
MONGO_DB=supertmarket
MONGO_PROTOCOL=mongodb+srv
```

---

## Uso con Docker Compose

1. Construye y levanta los servicios:
   ```sh
   docker-compose up --build
   ```
2. Accede a la API en: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Uso local (sin Docker)

1. Instala dependencias:
   ```sh
   pip install -r requirements.txt
   ```
2. Asegúrate de tener MongoDB corriendo y el `.env` configurado.
3. Ejecuta la app:
   ```sh
   uvicorn app.main:app --reload
   ```

---

## Endpoints principales

- **Usuarios:** `/users/`
- **Productos:** `/products/`
- **Ventas:** `/sales/`
- **Movimientos de caja:** `/cash-movements/`
- **Cuentas de cliente:** `/client-accounts/`
- **Estados de caja diaria:** `/daily-cash-status/`
- **Configuraciones:** `/settings/`
- **Consulta por código de barras:** `/products/barcode/{barcode}`

### Ejemplo de consulta por código de barras

```
GET /products/barcode/7622210449283
```

Devuelve información del producto desde OpenFoodFacts.

---

## Notas de seguridad

- Cambia las contraseñas por defecto en producción.
- Si usas MongoDB Atlas, asegúrate de restringir el acceso por IP y usar usuarios con permisos mínimos.

---

## Licencia

MIT
