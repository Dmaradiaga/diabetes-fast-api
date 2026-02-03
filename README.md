# API de Predicción de Diabetes

API simple con FastAPI que carga un modelo de ML desde DagshHub para predecir diabetes.

## Estructura del Proyecto

```
diabetes-fast-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicación FastAPI

## Instalación Rápida

### 1. Instalar dependencias

Copia `.env` a `.env` y configura tus credenciales:

```bash
cp .env .env
```

Edita `.env`:

```env
DAGSHUB_USERNAME=tu_usuario
DAGSHUB_REPO=owner/repo
MLFLOW_TRACKING_URI=https://dagshub.com/owner/repo.mlflow
MODEL_NAME=diabetes-model
```

### 3. Ejecutar

```bash

La API estará en: `http://localhost:8000`

## Documentación

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc


GET /api/health
```

### Predicción

```bash
POST /api/predict
```

**Ejemplo:**

```bash
curl -X POST "http://localhost:8000/api/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "pregnancies": 6,
    "glucose": 148,
    "blood_pressure": 72,
    "skin_thickness": 35,
    "insulin": 0,
    "bmi": 33.6,
    "diabetes_pedigree_function": 0.627,
    "age": 50
  }'
```

**Respuesta:**

```json
{
  "prediction": 1,
  "message": "Diabetes"
}
```

##  Datos de Entrada

| Campo | Descripción |
|-------|-------------|
| `pregnancies` | Número de embarazos |
| `glucose` | Glucosa en plasma |
| `blood_pressure` | Presión arterial (mm Hg) |
| `skin_thickness` | Grosor de la piel (mm) |
| `insulin` | Insulina (mu U/ml) |
| `bmi` | Índice de masa corporal |
| `diabetes_pedigree_function` | Función de pedigrí de diabetes |
| `age` | Edad (años) |

## Obtener Credenciales de DagshHub

1. Ve a [DagshHub](https://dagshub.com)
2. Crea una cuenta o inicia sesión
3. Ve a **Settings** → **Tokens**
4. Crea un token nuevo
5. Copia el token y tu username al `.env`

## Tecnologías

- **FastAPI**: Framework web
- **MLflow**: Gestión de modelos
- **DagshHub**: Almacenamiento de modelos
- **Pydantic**: Validación de datos

## Notas

- El modelo se carga automáticamente al iniciar
- Usa el stage "Production" del modelo en MLflow
- Todos los endpoints están documentados en `/docs`
