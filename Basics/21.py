l1 = ["Car", "Plane", "Boat"]
num = (1,3,5)
for idx, (i,n) in enumerate(zip(l1,num), start=1):
    print(f"Index: {idx}, Vehicle: {i}, Value: {n}")