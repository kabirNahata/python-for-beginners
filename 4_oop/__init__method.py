# The __init__ method lets you set initial values when creating an object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Kabir", 16)
print("Name:", p1.name)
print("Age:", p1.age)
