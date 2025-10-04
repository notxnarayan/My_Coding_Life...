#1. Create a text file and write name, age, and city
name = "John"
age = 26
city = "Ernakulam"
with open("Test.txt", "w") as file:
    file.writelines(f"Name: {name} \n")
    file.write(f"Age: {age}\n")
    file.writelines(f"City: {city}\n")