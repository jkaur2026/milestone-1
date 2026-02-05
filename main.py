from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from pathlib import Path
from typing import List, Optional 

app = FastAPI(title="Milestone 1")

ModelPath = Path(__file__).parent/"model.pkl"
model = joblib.load(ModelPath)

class PredictionRequest(BaseModel):
    features: List[float]

class PredictionResponse(BaseModel):
    prediction: int
    probabilities: Optional[List[float]] = None

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    x = [request.features]
    pred = int(model.predict(x)[0])
    return PredictionResponse(prediction=pred)
