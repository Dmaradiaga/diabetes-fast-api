# --- Etapa 1: Construcción ---
FROM python:3.10-slim AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Instalar herramientas necesarias para compilar algunas librerías
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crear un entorno virtual para aislar las dependencias
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# --- Etapa 2: Imagen Final ---
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Instalar git (necesario para dagshub/gitpython)
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copiar solo el entorno virtual desde la etapa de construcción
COPY --from=builder /opt/venv /opt/venv

# Copiar el código de la aplicación
COPY . .

# Exponer el puerto
EXPOSE 8000

# Asegurar que el token de DagshHub se pase como variable de entorno de API
ENV DAGSHUB_API_TOKEN=""

# Comando para ejecutar con Gunicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.main:app", "--bind", "0.0.0.0:8000"]
