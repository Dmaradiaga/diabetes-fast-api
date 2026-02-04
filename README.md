# API de Prediccion de Diabetes

Esta es una aplicacion sencilla creada con FastAPI que utiliza un modelo de inteligencia artificial para predecir si una persona podria tener diabetes. El modelo se carga de forma automatica desde DagshHub.

## Requisitos Previos

Antes de comenzar, necesitas tener instalado:
- Python 3.10 o superior.
- Una cuenta en DagshHub.

## Configuracion

1. Crea un archivo llamado .env en la carpeta principal del proyecto.
2. Copia y pega el siguiente contenido en el archivo .env y completa con tus datos de DagshHub:

```env
DAGSHUB_USERNAME=tu_usuario
DAGSHUB_REPO_NAME=tu_repositorio
MLFLOW_TRACKING_URI=https://dagshub.com/tu_usuario/tu_repositorio.mlflow
MODEL_NAME=diabetes-model
```

## Instalacion

1. Abre una terminal en la carpeta del proyecto.
2. Instala todas las librerias necesarias con el siguiente comando:

pip install -r requirements.txt

## Como ejecutar la API

Para iniciar el servidor, ejecuta el siguiente comando:

```bash
python -m app.main
```

Una vez ejecutado, la API estara disponible en: http://localhost:8000

## Como probar la API

### 1. Documentacion interactiva
Puedes ver y probar todos los servicios de la API desde tu navegador en:
http://localhost:8000/docs

### 2. Verificar estado
Puedes revisar si la API y el modelo estan funcionando correctamente en:
http://localhost:8000/api/health

### 3. Realizar una prediccion
Para obtener una prediccion, debes enviar una solicitud de tipo POST a la ruta:
http://localhost:8000/api/predict

Ejemplo de datos que debes enviar (en formato JSON):

```json
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
```

## Datos necesarios para la prediccion

- pregnancies: Numero de embarazos.
- glucose: Nivel de glucosa en la sangre.
- blood_pressure: Presion arterial.
- skin_thickness: Grosor de la piel.
- insulin: Nivel de insulina.
- bmi: Indice de masa corporal.
- diabetes_pedigree_function: Funcion de herencia de diabetes.
- age: Edad del paciente.

## Estructura del proyecto

- app/main.py: Punto de inicio de la aplicacion.
- app/api/: Definicion de las rutas o servicios.
- app/services/: Logica para cargar el modelo y realizar predicciones.
- app/models/: Definicion de como deben lucir los datos de entrada.
- requirements.txt: Lista de librerias necesarias.
