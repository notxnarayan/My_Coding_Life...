num = int(input("Enter the number: "))
s = 0

while num>0:
    s = s +(num%10)
    num //=10

print(s)