d = {}
while True:
     i = input("Enter the product name (exit to quit): ")
     if "exit" in i:
          print("Exiting...")
          break
     else:
          val = int(input("Enter the cost of the product: "))

     if i and val:
          d[i] = val
sum = 0
for i in d.keys():
     sum += d[i]
print(d, f"Sum is {sum}")
