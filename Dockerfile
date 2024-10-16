FROM python:3.10-slim-bullseye

# Actualizamos los repositorios e instalamos las dependencias necesarias
RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    libpq-dev \
    python3-psycopg2 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . .

# Añadir el archivo requirements.txt e instalar las dependencias de Python
RUN pip install -r requirements.txt

# Exponer el puerto 5001 para Flask
EXPOSE 5004

# Comando para ejecutar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]