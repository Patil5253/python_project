import pandas as pd
from textblob import TextBlob

def analyze_sentiment():
    df = pd.read_csv("data/reviews.csv")

    sentiment_scores = {}

    for _, row in df.iterrows():
        product = row["Product"]
        review = row["Review"]

        polarity = TextBlob(review).sentiment.polarity
        sentiment_scores[product] = polarity

    return sentiment_scores
