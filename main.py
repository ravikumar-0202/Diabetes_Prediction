from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("classifier.pkl", "rb") as f:
    classifier = pickle.load(f)

class PatientData(BaseModel):
    pregnancies: float
    glucose: float
    blood_pressure: float
    skin_thickness: float
    insulin: float
    bmi: float
    diabetes_pedigree_function: float
    age: float

@app.post("/predict")
def predict(data: PatientData):
    features = np.array([[
        data.pregnancies,
        data.glucose,
        data.blood_pressure,
        data.skin_thickness,
        data.insulin,
        data.bmi,
        data.diabetes_pedigree_function,
        data.age
    ]])

    std_features = scaler.transform(features)
    prediction = classifier.predict(std_features)[0]
    score = classifier.decision_function(std_features)[0]
    confidence = min(100, max(0, int(50 + score * 15)))

    return {
        "prediction": int(prediction),
        "probability": confidence,
        "risk_level": "High" if prediction == 1 else "Low",
        "result": "Diabetic" if prediction == 1 else "Not Diabetic"
    }
