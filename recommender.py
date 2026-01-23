from src.mba import run_mba
from src.sentiment import analyze_sentiment

def recommend(product_name):
    rules = run_mba()
    sentiments = analyze_sentiment()

    recommendations = []

    for _, row in rules.iterrows():
        antecedents = list(row['antecedents'])
        consequents = list(row['consequents'])

        if product_name in antecedents:
            for item in consequents:
                if sentiments.get(item, 0) > 0:
                    recommendations.append(item)

    return list(set(recommendations))
