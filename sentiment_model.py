import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_sentiment_model():
    df = pd.read_csv("data/reviews.csv")

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(df["review"])
    y = df["label"]

    model = MultinomialNB()
    model.fit(X, y)

    df["prediction"] = model.predict(X)
    return df


