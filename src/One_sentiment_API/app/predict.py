from pathlib import Path
import pickle
import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
import spacy
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


BASE_DIR = Path(__file__).resolve().parent.parent.parent



def load_new_string(input_string: str):
    # Preparando a string recebida para analise
    df = pd.DataFrame([input_string], columns=['text'])
    nlp = spacy.load("pt_core_news_sm")
    nltk.download('stopwords')
    nltk.download('wordnet')
    stop_words = nltk.corpus.stopwords.words('portuguese')
    working_text = df["text"]
    tokenization = [nlp(text.lower()) for text in working_text]
    nltk.download('wordnet', download_dir='../data/kaggle/working/nltk_data')
    nltk.data.path.append("../data/kaggle/working/nltk_data")

    from nltk.stem import PorterStemmer
    ps = PorterStemmer()

    # aplicando stemming e removendo stop words, pontuações, mentions e links
    new_text = []
    for phrase in tokenization:
        new_phrase = ""
        for token in phrase:
            if not str(token) in stop_words and not token.is_punct and "@" not in str(token) and "http" not in str(token):
                new_phrase += ps.stem(str(token)) + " "
        new_text.append(new_phrase[:-1])

    df["text"] = new_text
    return df



def load_model(model: str):
    models_dir = BASE_DIR / "models"
    mapping = {
        'LogisticRegression': 'lrUCV_model.pkl',
        'lrUCV': 'lrUCV_model.pkl',
        'DecisionTreeClassifier': 'dtrUCV_model.pkl',
        'dtcUCV': 'dtrUCV_model.pkl',
        'RandomForestClassifier': 'rfcUCV_model.pkl',
        'rfcUCV': 'rfcUCV_model.pkl',
        'MultinomialNB': 'mnbUCV_model.pkl',
        'mnbUCV': 'mnbUCV_model.pkl',
    }
    filename = mapping.get(model)
    if filename is None:
        raise ValueError(f"Unknown model '{model}'. Available: {list(mapping.keys())}")
    model_path = models_dir / filename
    if not model_path.exists():
        raise FileNotFoundError(f"Model file not found: {model_path}")
    with model_path.open('rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def load_vectorizer(vectorizer_path: str):
    vectorizer_path = Path(vectorizer_path)
    if not vectorizer_path.exists():
        raise FileNotFoundError(f"Vectorizer file not found: {vectorizer_path}")
    with vectorizer_path.open('rb') as file:
        vectorizer = pickle.load(file)
    return vectorizer

def transform_input(df: pd.DataFrame, vectorizer) -> any:
    # Transformando a string de entrada
    X_input = vectorizer.transform(df['text'])
    return X_input

def predict_sentiment(model, X_input):
    prediction = model.predict(X_input)
    sentiment = "positive" if prediction[0] == 1 else "negative"
    accuracy_score = model.score(X_input, prediction)
    return prediction, sentiment, accuracy_score

def main(string: str, model: str):
    df = load_new_string(string)
    model = load_model(model)
    vectorizer = load_vectorizer(BASE_DIR / 'models' / 'vect_uni_cv.pkl')
    X_input = transform_input(df, vectorizer)
    prediction, sentiment, score = predict_sentiment(model, X_input)
    print(f'Sentiment: {sentiment}, Score: {score:.2f}, Prediction: {prediction[0]}')
    return sentiment, score


if __name__ == "__main__":
    main()