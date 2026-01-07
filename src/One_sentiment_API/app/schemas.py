from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str

class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    model: str = "dummy-sentiment-model-v1"
    score: float = 0.99
