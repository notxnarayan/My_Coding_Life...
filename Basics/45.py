fruit = ["Apple", "Orange", "PassionFruit"]
price = [23, 456, 5]

for idx, (f, p) in enumerate(zip(fruit, price)):
    print(f"{f:<12} | {p:>5}")