class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is Speaking....")

class Employee(Person):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        self.hour = 7

    def work(self):
        print(f"{self.name} is Working....")

class Manager(Employee, Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.hour = 9

    def manage(self):
        self.work()
        print(f"{self.name} is Managing....")

p = Person("Walker")
print(p.name)

emp = Employee("Hans", 65)
print(emp.hour)
print(emp.name)
emp.work()
emp.speak()

mngr = Manager("Alex", 45)
mngr.manage()
mngr.speak()
print(mngr.hour)
