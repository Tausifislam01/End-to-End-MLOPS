import subprocess
import sys

from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

from end_to_end_mlops.pipeline.prediction import PredictionPipeline


app = FastAPI(title="Wine Quality Prediction")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")


@app.get("/train")
async def train():
    result = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)
    if result.returncode != 0:
        return JSONResponse(status_code=500, content={"status": "failed", "error": result.stderr})
    return {"status": "training completed"}


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    fixed_acidity: float = Form(...),
    volatile_acidity: float = Form(...),
    citric_acid: float = Form(...),
    residual_sugar: float = Form(...),
    chlorides: float = Form(...),
    free_sulfur_dioxide: float = Form(...),
    total_sulfur_dioxide: float = Form(...),
    density: float = Form(...),
    pH: float = Form(...),
    sulphates: float = Form(...),
    alcohol: float = Form(...),
):
    data = {
        "fixed acidity": fixed_acidity,
        "volatile acidity": volatile_acidity,
        "citric acid": citric_acid,
        "residual sugar": residual_sugar,
        "chlorides": chlorides,
        "free sulfur dioxide": free_sulfur_dioxide,
        "total sulfur dioxide": total_sulfur_dioxide,
        "density": density,
        "pH": pH,
        "sulphates": sulphates,
        "alcohol": alcohol,
    }
    predictor = PredictionPipeline()
    prediction = predictor.predict(data)[0]
    return templates.TemplateResponse(request, "index.html", {"prediction": round(float(prediction), 3)})


@app.post("/api/predict")
async def api_predict(payload: dict):
    predictor = PredictionPipeline()
    prediction = predictor.predict(payload)[0]
    return {"prediction": float(prediction)}
