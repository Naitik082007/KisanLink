from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.linear_model import LinearRegression

app = FastAPI(title="KisanLink Analytics")

class PricePoint(BaseModel):
    date: str
    price: float

class ForecastRequest(BaseModel):
    history: list[PricePoint]
    horizon: int = 7

@app.get("/health")
def health():
    return {"ok": True, "service": "kisanlink-analytics"}

@app.post("/forecast")
def forecast(req: ForecastRequest):
    df = pd.DataFrame([p.model_dump() for p in req.history])
    if len(df) < 3:
        return {"forecast": [], "message": "At least 3 observations are required."}
    X = pd.DataFrame({"t": range(len(df))})
    y = df["price"]
    model = LinearRegression().fit(X, y)
    future = [[len(df)+i] for i in range(req.horizon)]
    preds = model.predict(future)
    return {
        "method": "linear baseline",
        "forecast": [round(float(x),2) for x in preds],
        "note": "Prototype baseline only; production forecasting should use validated commodity-specific models and official price/arrival data."
    }
