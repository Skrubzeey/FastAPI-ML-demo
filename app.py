from fastapi import FastAPI, HTTPException
import numpy as np
from pydantic import BaseModel
import joblib
from sklearn.datasets import load_wine
import os
import redis

# zaladowanie modelu oraz skalera
model = joblib.load('wine_model.pkl')
scaler = joblib.load('scaler.pkl')
data = load_wine()
expected_features = data.data.shape[1]

# stworzenie aplikacji fastapi
app = FastAPI()

# połączenie się z bazą danych redis
redis_client = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=int(os.getenv("REDIS_PORT", 6379)))


class WineInput(BaseModel):
    features: list[float]


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}


@app.post("/predict")
def predict(data: WineInput):
    if len(data.features) != expected_features:
        raise HTTPException(status_code=400, detail=f"Expected {expected_features} features, got {len(data.features)}")

    try:
        X_input = np.array([data.features])
        X_scaled = scaler.transform(X_input)
        prediction = model.predict(X_scaled)[0]
        return {"predicted_class": int(prediction)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/info")
def get_model_info():
    return {
        "model_type": type(model).__name__,
        "num_features": expected_features,
        "dataset": "Wine Dataset (sklearn)"
    }


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/redis_check")
def redis_status():
    redis_client.set("message", "Hello from Redis!")
    return {"redis_message": redis_client.get("message").decode("utf-8")}
