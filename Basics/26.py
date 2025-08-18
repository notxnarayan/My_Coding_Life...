"""🎯 Program Requirements:
Allow the user to enter multiple books with:

Book title (string)

Author (string)

Price (float)

Quantity (int)

Use loop and condition to:

Add multiple books

Search a book by title

Show total value of all books in library (price × quantity)

Display a formatted book list and total inventory value."""

all_books = []
def find_book(title):
    for i in all_books:
        if i["Title"].lower() == title.lower():
            price1 = i["Price"]
            quantity1= i["Quantity"]
            print("Book is found!")
            print(f"Title: {i["Title"]}, Author: {i["Author"]}, Price: {i["Price"]}, Quantity: {i["Quantity"]}")
            print(f"Total value: {price1*quantity1}")


def book():
    book = {}
    addag = input("What do you want to do? ")
    if "no" in addag.lower():
        return
    elif "add" in addag.lower():
        book["Title"] = input("Enter the book title: ")
        book["Author"] = input("Enter the author: ")
        book["Price"] = float(input("Enter the price: "))
        book["Quantity"] = float(input("Enter the quantity: "))
        return book
    elif "search" in addag.lower():
        search_book()

def search_book():
    sbk = input("Enter the name of the book you want to search (exit to quit): ")
    if "exit" in sbk.lower():
        return None
    find_book(sbk)

while True:
    bk = book()
    if bk is None:
        break
    all_books.append(bk)

for idx,i in enumerate(all_books, start=1):
    print(f"{idx}. Title: {i["Title"]}, Author: {i["Author"]}, Price: {i["Price"]}, Quantity: {i["Quantity"]}")

invval = 0
for i in all_books:
    price = i["Price"]
    quantity = i["Quantity"]
    if price is not None and quantity>1:
        invval +=price*quantity



