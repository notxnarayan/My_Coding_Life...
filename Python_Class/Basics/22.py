l1 = ["Car", "Plane", "Boat"]
num = (1,3,5)
ziped = []
for idx, zipd in enumerate(zip(l1,num), start=1):
    ziped.append(zipd)
print(ziped)
ziped, num = zip(*ziped)
print(list(ziped), num)