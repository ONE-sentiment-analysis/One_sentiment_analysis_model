from pydantic import BaseModel
from enum import Enum

class SentimentRequest(BaseModel):
    text: str
    model: str = "lr"

class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    model: str
    score: float

class MLModels(str, Enum):
    NaiveBayes = "nb"
    LogisticRegression = "lr"
    RandomForest = "rf"