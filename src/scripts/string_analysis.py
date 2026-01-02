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


parser = argparse.ArgumentParser(description="Calculate sentiment of given satring.")
parser.add_argument("-s", "--string", help="String to be analyzed.")
parser.add_argument("-m", "--model", help="Trained model to be used.")
args = parser.parse_args()


with open('../models/rfcUCV_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


def main():
    result = loaded_model.predict([args.string])
    print(f"Sentiment analysis result: {result[0]}")


if __name__ == "__main__":
    main()