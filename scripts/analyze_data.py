import pandas as pd
import matplotlib.pyplot as plt

# Load the stock data
df = pd.read_csv("../data/stock_prices.csv", index_col=0)

# Plot stock prices
plt.figure(figsize=(10, 5))
for col in df.columns:
    plt.plot(df.index, df[col], label=col)

plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title("Stock Prices Over Last 7 Days")
plt.legend()
plt.xticks(rotation=45)
plt.grid()

# Save plot
plt.savefig("../data/stock_trend.png")
print("Stock trend analysis completed!")
