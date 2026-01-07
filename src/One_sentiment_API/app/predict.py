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
    match model:
        case 'RandomForestClassifier' | 'rfcUCV':
            model_path = 'src/models/rfcUCV_model.pkl'
        case 'DecisionTreeClassifier' | 'dtcUCV':
            model_path = 'src/models/dtcUCV_model.pkl'
        case 'LogisticRegression' | 'lrUIDF':
            model_path = 'src/models/lrUCV_model.pkl'
        case 'MultinomialNB' | 'mnbUIDF':
            model_path = 'src/models/mnbUIDF_model.pkl'
    
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def load_vectorizer(vectorizer_path: str):
    with open(vectorizer_path, 'rb') as file:
        vectorizer = pickle.load(file)
    return vectorizer

def transform_input(df: pd.DataFrame, vectorizer) -> any:
    # Transformando a string de entrada
    X_input = vectorizer.transform(df['text'])
    return X_input

def predict_sentiment(model, X_input) -> str:
    prediction = model.predict(X_input)
    sentiment = "positive" if prediction[0] == 1 else "negative"
    accuracy_score = model.score(X_input, prediction)
    return sentiment, accuracy_score

def main(string: str, model: str):
    df = load_new_string(string)
    model = load_model(model)
    vectorizer = load_vectorizer('src/models/vect_uni_cv.pkl')
    X_input = transform_input(df, vectorizer)
    sentiment, score = predict_sentiment(model, X_input)
    print(f'Sentiment: {sentiment}, Score: {score:.2f}')


if __name__ == "__main__":
    main()