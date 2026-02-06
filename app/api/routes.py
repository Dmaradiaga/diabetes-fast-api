"""
Rutas de la API.
"""
from fastapi import APIRouter, HTTPException
import logging

from app.models.schemas import DiabetesInput
from app.services import predictor
from app.services import model_loader

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get("/health")
async def health():
    """Verifica el estado de la API y muestra información del modelo."""
    return {
        "status": "ok",
        "model_loaded": model_loader.model is not None,
        "model_metrics": model_loader.get_metrics()
    }


@router.post("/predict")
async def predict_diabetes(data: DiabetesInput):
    """
    Predice si un paciente tiene diabetes.
    
    Ejemplo de entrada:
    {
        "pregnancies": 6,
        "glucose": 148,
        "blood_pressure": 72,
        "skin_thickness": 35,
        "insulin": 0,
        "bmi": 33.6,
        "diabetes_pedigree_function": 0.627,
        "age": 50
    }
    """
    try:
        result = predictor.predict(data)
        return result
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
