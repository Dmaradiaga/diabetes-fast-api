"""
Servicio para cargar modelos desde DagshHub.
"""
import os
from dotenv import load_dotenv

# CARGAR VARIABLES DE ENTORNO ANTES QUE NADA
load_dotenv(override=True)

import mlflow
from mlflow.tracking import MlflowClient
import logging
import dagshub
import dagshub.auth

logger = logging.getLogger(__name__)

# Variable global para almacenar el modelo y sus métricas
model = None
model_metrics = None


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
    """Carga el modelo y sus métricas desde DagshHub/MLflow."""
    global model, model_metrics
    try:
        setup_dagshub()
        
        # Obtener el nombre del modelo
        model_name = os.getenv("MODEL_NAME")
        
        # Cargar modelo desde Staging
        model_uri = f"models:/{model_name}/Staging"
        logger.info(f"Intentando cargar: {model_uri}")
        model = mlflow.pyfunc.load_model(model_uri)
        logger.info(f"Modelo cargado exitosamente: {model_uri}")
        
        # Cargar métricas
        try:
            client = MlflowClient()
            # Obtener la versión del modelo en Staging
            latest_versions = client.get_latest_versions(model_name, stages=["Staging"])
            if latest_versions:
                run_id = latest_versions[0].run_id
                run_data = client.get_run(run_id).data
                model_metrics = run_data.metrics
                logger.info(f"Métricas del modelo cargadas: {model_metrics}")
            else:
                logger.warning(f"No se encontró una versión en 'Staging' para obtener métricas")
        except Exception as me:
            logger.error(f"Error al cargar las métricas: {repr(me)}")
            model_metrics = {"error": "No se pudieron cargar las métricas"}

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


def get_metrics():
    """Obtiene las métricas del modelo cargado."""
    return model_metrics
