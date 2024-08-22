# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY app.py /app/

# Copia el archivo de dependencias al contenedor
COPY requirements.txt /app/

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que la aplicación Flask se ejecutará
EXPOSE 8000

# Define el comando para ejecutar la aplicación Flask
CMD ["python", "app.py"]