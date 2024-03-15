# Etapa de construcción
FROM python:3.10 AS builder

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /build

# Instala wait-for-it
RUN apt-get update && apt-get install -y wget
RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod +x wait-for-it.sh

COPY requirements.txt requirements.txt

# Instala dependencias en una etapa separada
RUN python -m venv /venv && \
    /venv/bin/pip install --no-cache-dir --upgrade pip && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Etapa final
FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Copia solo los archivos necesarios de la etapa de construcción
COPY --from=builder /venv /venv
COPY --from=builder /build/wait-for-it.sh /code/wait-for-it.sh
COPY --from=builder /build .

# Cambia al usuario no root
RUN useradd -ms /bin/bash appuser
USER appuser
CMD ["python", "manage.py", "migrate"]
# Activa el entorno virtual
ENV PATH="/venv/bin:$PATH"

# Agrega más comandos de migración según tus bases de datos
# Elimina archivos temporales y cachés, pero no falla si no se encuentran
RUN find -name "__pycache__" -exec rm -r {} + || true
CMD ["python", "manage.py", "migrate"]

# Arranca la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:4545"]
