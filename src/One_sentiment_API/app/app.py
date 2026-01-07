from fastapi import FastAPI, HTTPException
from app.schemas import SentimentRequest

app = FastAPI()

@app.get("/welcome")
def welcome():
	return {"message": "Welcome to the One Sentiment API!"}

@app.get("/models")
def list_models():
    return {"models": ["dummy-sentiment-model-v1"]}

@app.post("/predict_sentiment")
def predict_sentiment(request: SentimentRequest) -> SentimentRequest:
    text = request.text
    if not text:
        raise HTTPException(status_code=400, detail="Text input is required.")
    # Dummy sentiment analysis logic
    sentiment = "positive" if "good" in text.lower() else "negative"
    return {"text": text, "sentiment": sentiment}