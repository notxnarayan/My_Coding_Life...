class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

class Human:
    def speak(self):
        print("Hello!")

d = Dog()
c = Cat()
h = Human()

creatures = [d, c, h]

for creature in creatures:
    creature.speak()
