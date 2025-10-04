"""Create a class Student to store name, roll number, and marks of 3 subjects.
Include methods to calculate total, average, and display all details. Use encapsulation for data protection."""

subjects = ["Maths", "Science", "English"]
class Student:
    def __init__(self):
        self.__name = input(f"Enter the student's name: ")
        self.__rolln = int(input(f"Enter the roll number of {self.__name}: "))
        self.__marks = {}
        for idx, i in enumerate(subjects, start = 1):
            self.__totalsubs = idx
            self.__marks[i] = int(input(f"Enter mark of {self.__name} in {i}: "))
        avsum = 0
        for key in self.__marks: avsum += self.__marks[key]
        self.__ave = avsum/self.__totalsubs
        self.__totalmarks = 0
        for i in self.__marks:
            self.__totalmarks+=self.__marks[i]


    def ask(self):
        userinput = input("What would you like to see: ")
        if "average" in userinput.lower():
            print(f"The average marks of {self.__name} is {round(self.__ave)}")

        elif "total" in userinput.lower():
            print(f"The average marks of {self.__name} is {self.__totalmarks}")

        elif "details" in userinput.lower():
            print(f"|Name:         | {self.__name}      ")
            print(f"|Roll Number:  | {self.__rolln}     ")
            print(f"|Average marks:| {round(self.__ave)}")
            print(f"|Total marks:  | {self.__totalmarks}")





s = Student()
s.ask()