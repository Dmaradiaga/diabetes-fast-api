"""
Modelos de datos para la API.
"""
from pydantic import BaseModel, Field


class DiabetesInput(BaseModel):
    """Datos de entrada para predicción de diabetes."""
    
    pregnancies: int = Field(..., ge=0, description="Número de embarazos")
    glucose: float = Field(..., ge=0, description="Glucosa en plasma")
    blood_pressure: float = Field(..., ge=0, description="Presión arterial (mm Hg)")
    skin_thickness: float = Field(..., ge=0, description="Grosor de la piel (mm)")
    insulin: float = Field(..., ge=0, description="Insulina (mu U/ml)")
    bmi: float = Field(..., ge=0, description="Índice de masa corporal")
    diabetes_pedigree_function: float = Field(..., ge=0, description="Función de pedigrí")
    age: int = Field(..., ge=0, description="Edad (años)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "pregnancies": 6,
                "glucose": 148.0,
                "blood_pressure": 72.0,
                "skin_thickness": 35.0,
                "insulin": 0.0,
                "bmi": 33.6,
                "diabetes_pedigree_function": 0.627,
                "age": 50
            }
        }
