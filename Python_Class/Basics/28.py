class Person:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("Speaking....")

class Student(Person):
    def study(self):
        print("Studying....")

class Employee(Person):
    def __init__(self,name):
        self.hour = 7
    def work(self):
        print("Working....")

p = Person("Walker")
print(p.name)
st = Student("Alan")
mply = Employee("Hans")
print(mply.hour)
print(mply.name)
st.study()
st.speak()
mply.work()
mply.speak()