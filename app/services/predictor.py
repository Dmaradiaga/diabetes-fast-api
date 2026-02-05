"""
Servicio de predicción.
"""
import logging

from app.services.model_loader import get_model
from app.models.schemas import DiabetesInput

logger = logging.getLogger(__name__)


def predict(input_data: DiabetesInput) -> dict:
    """
    Realiza una predicción de diabetes.
    
    Args:
        input_data: Datos del paciente
        
    Returns:
        dict con la predicción
    """
    try:
        # Usar un diccionario de listas para satisfacer el esquema del modelo sin pandas
        data = {
            'Pregnancies': [float(input_data.pregnancies)],
            'Glucose': [float(input_data.glucose)],
            'BloodPressure': [float(input_data.blood_pressure)],
            'SkinThickness': [float(input_data.skin_thickness)],
            'Insulin': [float(input_data.insulin)],
            'BMI': [float(input_data.bmi)],
            'DiabetesPedigreeFunction': [float(input_data.diabetes_pedigree_function)],
            'Age': [float(input_data.age)]
        }
        
        # Hacer predicción usando el diccionario directamente
        model = get_model()
        prediction = int(model.predict(data)[0])
        
        return {
            "prediccion": prediction,
            "mensaje": "Diabetes" if prediction == 1 else "No diabetes"
        }
        
    except Exception as e:
        logger.error(f"Error en predicción: {e}")
        raise
