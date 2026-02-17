import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Loading data...")

sentiment = pd.read_csv("data/fear_greed_index.csv")
trades = pd.read_csv("data/historical_data.csv")

print("Data loaded successfully.\n")

sentiment['date'] = pd.to_datetime(sentiment['date'], errors='coerce')
sentiment['date'] = sentiment['date'].dt.normalize()


trades['Timestamp'] = pd.to_datetime(
    trades['Timestamp'],
    unit='ms',
    errors='coerce'
)

trades['date'] = trades['Timestamp'].dt.normalize()

trades['Closed PnL'] = pd.to_numeric(trades['Closed PnL'], errors='coerce')
trades = trades.dropna(subset=['Closed PnL'])

print("Trader date range:",
      trades['date'].min(), "to", trades['date'].max())

print("Sentiment date range:",
      sentiment['date'].min(), "to", sentiment['date'].max())


merged = trades.merge(
    sentiment[['date','classification']],
    on='date',
    how='left'
)

print("Merged shape:", merged.shape)

print("Missing classification after merge:",
      merged['classification'].isnull().sum())


merged = merged.dropna(subset=['classification'])

print("Shape after removing missing classification:",
      merged.shape)


merged['win'] = merged['Closed PnL'] > 0

print("\nOverall Win Rate:", merged['win'].mean())

print("\nAverage PnL by Sentiment:")
print(merged.groupby('classification')['Closed PnL'].mean())

print("\nNumber of Trades by Sentiment:")
print(merged.groupby('classification')['Account'].count())


trade_counts = merged['Account'].value_counts()
threshold = trade_counts.median()

frequent_accounts = trade_counts[trade_counts > threshold].index

merged['trader_type'] = merged['Account'].apply(
    lambda x: "Frequent" if x in frequent_accounts else "Less Frequent"
)

print("\nFrequent vs Less Frequent Performance:")
print(merged.groupby(['trader_type','classification'])['Closed PnL'].mean())

if not merged.empty:
    plt.figure(figsize=(8,5))
    sns.boxplot(x='classification', y='Closed PnL', data=merged)
    plt.title("PnL Distribution: Fear vs Greed")
    plt.tight_layout()

    plt.savefig("pnl_sentiment_plot.png")

    plt.show()
else:
    print("No matching dates found between datasets.")