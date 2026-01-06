#!/usr/bin/env python3 
from pathlib import Path
import argparse
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
from sklearn.feature_extraction.text import HashingVectorizer


parser = argparse.ArgumentParser(description="Calculate sentiment of given satring.")
parser.add_argument("-s", "--string", help="String to be analyzed.")
parser.add_argument("-m", "--model", help="Trained model to be used.")
args = parser.parse_args()

# Preparando a string recebida para analise
df = pd.DataFrame([args.string], columns=['text'])
lb = LabelEncoder()
# df['text'] = lb.fit_transform(df['text'])
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
# df['text'] = lb.fit_transform(df['text'])



with open('src/models/rfcUCV_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


def main():
    # Carregando o vetorizer salvo
    # with open('src/models/tfidf_vectorizer.pkl', 'rb') as file:
    #     vectorizer = pickle.load(file)
    # vectorizer = HashingVectorizer(ngram_range=(1,1), use_idf=True, norm='l2', stop_words=stop_words)
    vectorizer = HashingVectorizer(n_features=2**4, norm='l2', stop_words=stop_words)

    # Transformando a string de entrada
    vectorizer.fit(df['text'])
    X_input = vectorizer.transform(df['text'])

    # Fazendo a predição
    prediction = loaded_model.predict(X_input)

    # Mapeando a predição para o rótulo original
    sentiment = "Positivo" if prediction[0] == 1 else "Negativo"

    print(f"A análise de sentimento da string fornecida é: {sentiment}")


if __name__ == "__main__":
    main()