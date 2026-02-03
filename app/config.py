"""
Variables de entorno
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de DagshHub
DAGSHUB_USERNAME = os.getenv("DAGSHUB_USERNAME")
DAGSHUB_REPO_NAME = os.getenv("DAGSHUB_REPO_NAME")

# Configuración de MLflow
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MODEL_NAME = os.getenv("MODEL_NAME")

# Configuración de la API
APP_NAME = "Diabetes Prediccion API"
APP_VERSION = "0.1.0"
