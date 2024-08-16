from fastapi import FastAPI, UploadFile
from src.entities.model import ModelPredictor
import uvicorn


app = FastAPI()

model = ModelPredictor()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("model/load")
def load_model(model_file: UploadFile):
    model.load(model_file.filename)
    return {"status": "ok"}


@app.post("model/predict")
def get_prediction(body):
    pred = model.predict(body)
    return {"prediction": pred}


@app.get("model/history")
def get_history():
    history = model.get_history()
    return {"history": history}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")
