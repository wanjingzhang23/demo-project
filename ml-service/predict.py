from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# 加载模型
with open("ml-service/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: dict):
    bet_amount = data["bet_amount"]
    win_rate = data["win_rate"]
    session_time = data["session_time"]

    features = np.array([[bet_amount, win_rate, session_time]])
    prob = model.predict_proba(features)[0][1]

    return {"risk_score": float(prob)}