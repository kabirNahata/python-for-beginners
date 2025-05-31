# You can define methods (functions) inside classes

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

p1 = Person("Kabir")
p1.greet()
