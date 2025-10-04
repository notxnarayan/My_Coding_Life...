import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Seed for reproducibility (optional)
np.random.seed(42)

# Generate weekly sales data: 12 weeks × 4 products
data = np.random.randint(50, 200, (12, 4))
products = ['A', 'B', 'C', 'D']

# Create DataFrame
df = pd.DataFrame(data, columns=products)

# Plot line chart
plt.figure(figsize=(8,5))
for product in products:
    plt.plot(df.index + 1, df[product], label=product)  # index+1 for week numbers

plt.title("Weekly Sales of Products A–D")
plt.xlabel("Week")
plt.ylabel("Sales")
plt.legend(title="Products")
plt.grid(True)
plt.show()
