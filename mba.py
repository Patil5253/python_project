import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def run_mba():
    data = pd.read_csv("data/transactions.csv")

    basket = (data
              .groupby(['Transaction_ID', 'Product'])['Product']
              .count().unstack().fillna(0))

    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    freq_items = apriori(basket, min_support=0.3, use_colnames=True)

    rules = association_rules(freq_items, metric="confidence", min_threshold=0.6)

    return rules[['antecedents', 'consequents', 'confidence']]
print("mba.py loaded successfully")
