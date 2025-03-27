import joblib
import numpy as np
import os

MODEL_PATH = 'model/tb_diabetes_model.pkl'
SCALER_PATH = 'model/scaler.pkl'

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

def predict_diabetes(input_data):
    features = np.array(list(input_data.values())).reshape(1, -1)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][prediction]
    return int(prediction), float(probability)
