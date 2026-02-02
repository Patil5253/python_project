import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def market_basket():
    df = pd.read_csv("data/transactions.csv")

    transactions = df.groupby("transaction_id")["product"].apply(list).tolist()

    te = TransactionEncoder()
    te_data = te.fit(transactions).transform(transactions)
    encoded_df = pd.DataFrame(te_data, columns=te.columns_)

    freq_items = apriori(encoded_df, min_support=0.3, use_colnames=True)
    rules = association_rules(freq_items, metric="confidence", min_threshold=0.5)

    return rules

