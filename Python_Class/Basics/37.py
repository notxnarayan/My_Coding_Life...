class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Human:
    def speak(self):
        print("Hello!")

def make_them_speak(creature):

    creature.speak()
d = Dog()
c = Cat()
h = Human()
make_them_speak(d)
make_them_speak(c)
make_them_speak(h)


