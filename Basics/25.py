
def printsent(**args):
    nm1 = None
    vl1 = None
    for key,value in args.items():
        if key == "name":
            nm1 = value
        elif key == "value":
            vl1 = value
    print(f"Name: {nm1}, Value: {vl1}")

name = []
value = []
while True:
    nm = input("Enter the name (exit to quit): ")

    if "exit" in nm:
        break
    else: val = input("Enter the value: ")
    name.append(nm)
    value.append(val)

for idx,(nam,vl) in enumerate(zip(name,value)):
    printsent(name=nam,value = vl)
