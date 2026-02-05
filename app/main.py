"""
Aplicación FastAPI para predicción de diabetes.
"""
from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
import uvicorn

from app.api.routes import router
from app.services import model_loader
from app import config

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Carga el modelo al iniciar la app."""
    logger.info("Cargando modelo...")
    if model_loader.load_model():
        logger.info("Modelo cargado")
    else:
        logger.error("Error al cargar modelo")
    yield


# Crear app
app = FastAPI(
    title=config.APP_NAME,
    version=config.APP_VERSION,
    lifespan=lifespan
)

# Incluir rutas
app.include_router(router, prefix="/api")


@app.get("/")
async def root():
    """Endpoint raíz."""
    return {
        "message": "Diabetes Prediccion API",
        "docs": "/docs",
        "health": "/api/health"
    }


if __name__ == "__main__":
    # Aumentar el timeout para dar tiempo a que el modelo se descargue de DagshHub
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True, timeout_keep_alive=120)
