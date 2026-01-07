from fastapi import FastAPI, HTTPException
from app.schemas import SentimentRequest, SentimentResponse, MLModels
from app.predict import main as predict_main

app = FastAPI()

@app.get("/welcome")
def welcome():
	return {"message": "Welcome to the One Sentiment API!"}

@app.get("/models")
def list_models():
    return {"available_models": [model.value for model in MLModels]}

@app.post("/predict_sentiment")
def predict_sentiment(request: SentimentRequest) -> SentimentResponse:
    text = request.text
    model = request.model
    if not text:
        raise HTTPException(status_code=400, detail="Text input is required.")
    sentiment, score = predict_main(text, model)
    response = SentimentResponse(
        text=text,
        sentiment=sentiment,
        model=model,
        score=score
    )
    return response

