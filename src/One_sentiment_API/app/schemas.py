from pydantic import BaseModel
from enum import Enum

class SentimentRequest(BaseModel):
    text: str
    model: str = "LogisticRegression"

class SentimentResponse(BaseModel):
    text: str
    sentiment: str
    model: str = "LogisticRegression"
    score: float = 0.99

class MLModels(str, Enum):
    RANDOM_FOREST = 'RandomForestClassifier'
    DECISION_TREE = 'DecisionTreeClassifier'
    LOGISTIC_REGRESSION = 'LogisticRegression'
    MULTINOMIAL_NB = 'MultinomialNB'