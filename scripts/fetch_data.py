import yfinance as yf
import pandas as pd

# List of stock tickers
stocks = ["AAPL", "TSLA", "GOOGL", "MSFT"]

# Fetch data
data = {}
for stock in stocks:
    stock_data = yf.download(stock, period="7d", interval="1d")
    data[stock] = stock_data['Close']

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("../data/stock_prices.csv", index=True)
print("Stock data saved successfully!")
