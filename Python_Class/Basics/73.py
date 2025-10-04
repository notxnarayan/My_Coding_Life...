import numpy as np

np.random.seed(42)
fluctuations = np.random.normal(0, 1, 10)
prices = 100 + np.cumsum(fluctuations)

daily_returns = np.diff(prices) / prices[:-1] * 100
avg_price = prices.mean()
highest_price = prices.max()
lowest_price = prices.min()

print("prices:", prices)
print("Daily returns:", daily_returns)
print("Average pric:", round(avg_price, 2))
print("Highest price:", round(highest_price, 2))
print("Lowest price:", round(lowest_price, 2))
