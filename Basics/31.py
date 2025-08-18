class Person:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Speaking....")

class Employee(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
        self.hour = 7
    def work(self):
        print("Working....")

class Manager(Employee,Person):
    def __init__(self,name,age):
        #Employee.__init__(self,name)
        #Person.__init__(self,name)
        super(Manager,self).__init__(name,age)
        #super(Person,self).__init__(name)
        self.hour = 9
    def manage(self):
        super().work()
        print("Managing....")

p = Person("Walker")
print(p.name)
mply = Employee("Hans",65)
mngr = Manager("Alex",45)
print(mply.hour)
print(mply.name)
mply.work()
mply.speak()
mngr.manage()