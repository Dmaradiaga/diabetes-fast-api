"""
Servicio para cargar modelos desde DagshHub.
"""
import os
import mlflow
import logging
import dagshub
from app import config

logger = logging.getLogger(__name__)

# Variable global para almacenar el modelo
model = None


def setup_dagshub():
    """Configuración las credenciales de DagshHub."""
    token = os.getenv("DAGSHUB_TOKEN")
    if token:
        import dagshub.auth
        dagshub.auth.add_app_token(token)
        
    dagshub.init(repo_owner=config.DAGSHUB_USERNAME, repo_name=config.DAGSHUB_REPO_NAME, mlflow=True)
    logger.info(f"DagshHub configurado: {config.MLFLOW_TRACKING_URI}")


def load_model():
    """Carga el modelo desde DagshHub/MLflow."""
    global model
    try:
        setup_dagshub()
        
        # Cargar modelo desde Staging
        model_uri = f"models:/{config.MODEL_NAME}/Staging"
        logger.info(f"Intentando cargar: {model_uri}")
        model = mlflow.pyfunc.load_model(model_uri)
        logger.info(f"Modelo cargado exitosamente: {model_uri}")
        return True
        
    except Exception as e:
        logger.error(f"Error al cargar modelo: {e}")
        logger.error(f"Verifica que el modelo '{config.MODEL_NAME}' esté en stage 'Staging'")
        logger.error(f"URL: https://dagshub.com/{config.DAGSHUB_USERNAME}/{config.DAGSHUB_REPO_NAME}/models")
        return False


def get_model():
    """Obtiene el modelo cargado."""
    if model is None:
        raise RuntimeError("Modelo no cargado")
    return model
