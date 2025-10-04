class Person:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Speaking....")

class Employee(Person):
    def __init__(self,name):
        super().__init__(name)
        self.hour = 7
    def work(self):
        print("Working....")

class Manager(Employee):
    def __init__(self,name):
        super().__init__(name)
        self.hour = 9
    def manage(self):
        super().work()
        print("Managing....")

p = Person("Walker")
print(p.name)
mply = Employee("Hans")
mngr = Manager("Alex")
print(mply.hour)
print(mply.name)
mply.work()
mply.speak()
mngr.manage()