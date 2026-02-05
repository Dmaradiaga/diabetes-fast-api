"""
Servicio para cargar modelos desde DagshHub.
"""
import os
from dotenv import load_dotenv

# CARGAR VARIABLES DE ENTORNO ANTES QUE NADA
load_dotenv(override=True)

import mlflow
import logging
import dagshub
import dagshub.auth

logger = logging.getLogger(__name__)

# Variable global para almacenar el modelo
model = None


def setup_dagshub():
    """Configuración las credenciales de DagshHub."""
    # Recargar por si acaso hubo cambios asíncronos
    load_dotenv(override=True)
    
    token = os.getenv("DAGSHUB_TOKEN")
    repo_owner = os.getenv("DAGSHUB_USERNAME")
    repo_name = os.getenv("DAGSHUB_REPO_NAME")
    
    if token:
        # Forzar variables de entorno que dagshub y mlflow usan
        os.environ["DAGSHUB_API_TOKEN"] = token
        os.environ["MLFLOW_TRACKING_TOKEN"] = token
        # También usar el método de autenticación por librería
        dagshub.auth.add_app_token(token)
        
    dagshub.init(repo_owner=repo_owner, repo_name=repo_name, mlflow=True)
    logger.info("DagshHub configurado correctamente")


def load_model():
    """Carga el modelo desde DagshHub/MLflow."""
    global model
    try:
        setup_dagshub()
        
        # Obtener el nombre del modelo
        model_name = os.getenv("MODEL_NAME")
        
        # Cargar modelo desde Staging
        model_uri = f"models:/{model_name}/Staging"
        logger.info(f"Intentando cargar: {model_uri}")
        model = mlflow.pyfunc.load_model(model_uri)
        logger.info(f"Modelo cargado exitosamente: {model_uri}")
        return True
        
    except Exception as e:
        logger.error(f"Error al cargar modelo: {repr(e)}")
        model_name = os.getenv("MODEL_NAME")
        repo_owner = os.getenv("DAGSHUB_USERNAME")
        repo_name = os.getenv("DAGSHUB_REPO_NAME")
        logger.error(f"Verifica que el modelo '{model_name}' esté en stage 'Staging'")
        logger.error(f"URL: https://dagshub.com/{repo_owner}/{repo_name}/models")
        return False


def get_model():
    """Obtiene el modelo cargado."""
    if model is None:
        raise RuntimeError("Modelo no cargado")
    return model
