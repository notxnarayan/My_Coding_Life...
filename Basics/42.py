"""Create a Python program using classes to manage a food ordering system. The system should:

Show a food menu (items with price).

Allow the user to select multiple items and quantities.

Calculate total bill with GST (5%).

Save the order summary to a file.

Display a thank-you message with receipt."""

food = {"samosa": 15,
        "puffs": 25,
        "burger": 80,
        "french fries": 80,
        "pizza": 120,
        "cold drink": 30}
receipt = {}
def printfood():
    for idx, (key,value) in enumerate(food.items(),start=1):
        print(f"{idx}. {key} - ₹{value}")

printfood()

while True:
    order = input("Enter the item to order ('done' for closing the order):").lower()
    if "done" in order.lower():
        break
    elif order in food:
        quantity = int(input("Enter the quantity:"))
        if quantity <=0:
            print("Invalid number!")
        else:
            receipt[order] = quantity
    else:
        print("Item currently not available please choose from the below...")
        printfood()
billcost = 0
print("""

Your Receipt:
""")
for idx, (key,value) in enumerate(receipt.items(),start=1):
    itemprice = food[key]
    totalcost = itemprice*value
    print(f"""{key} x{value} @ ₹{itemprice} = ₹{totalcost}""")
    billcost+=totalcost

gstcost = (5/100)*billcost
print(f"""
Subtotal: ₹{billcost}
GST(5%): ₹{gstcost}
Total amount: ₹{billcost+gstcost}
""")

