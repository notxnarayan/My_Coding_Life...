#1. Create a text file and write name, age, and city
from functools import update_wrapper


def one():
    name = "John"
    age = 26
    city = "Ernakulam"
    with open("Test.txt", "w") as file:
        file.writelines(f"Name: {name} \n")
        file.write(f"Age: {age}\n")
        file.writelines(f"City: {city}\n")

def two():
    with open("Test2.txt", "r") as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        print("Characters:", len(content))
        print("Words:", len(words))
        print("Lines:", len(lines))

def three():
    with open("Test2.txt", "r") as file:
        print("\nFile contents:\n")
        print(file.read())

def four():
    with open("Test2.txt", "r") as src_file:
        data = src_file.read()
    with open("Test3.txt", "w") as dest_file:
        dest_file.write(data)

def five():
    with open("Test2.txt", "r") as file:
        print("Lines starting with a vowel:\n")
        for line in file:
            if line.strip() and line[0].lower() in 'aeiou':
                print(line.strip())

def six():
    with open("Test2.txt", "r") as file:
        lines = file.readlines()
    print("Lines in reverse order:\n")
    for line in reversed(lines):
            print(line.strip())

def seven():
    with open("Test2.txt", "r") as file:
        content = file.read()
    updated_content = content.replace("Alice", 'Alan')
    updated_content = updated_content.replace("her", 'his')
    updated_content = updated_content.replace("Her", 'His')
    updated_content = updated_content.replace("She", 'He')
    updated_content = updated_content.replace("she", 'he')

    with open("Test3.txt", "w") as file:
        file.write(updated_content)

seven()


