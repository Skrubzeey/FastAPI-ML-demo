FROM python:3.11

# Stworzenie katalogu roboczego
WORKDIR /app

# Skopiowanie plików aplikacji do kontenera
COPY . .

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Wystawienie portu na zewnątrz kontenera
EXPOSE 8000

# Komenda startowa do uruchomienia FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]