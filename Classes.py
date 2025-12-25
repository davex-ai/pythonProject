class Animal:
    def walk(self):
        print("walking")
class Dog(Animal): # Dog is inheriting walk from animal class
    def __init__(self, name, age): # This is a constructor
        self.name = name
        self.age = age


def bark(self):
    print(f"{self.name} barks\n WOOF!!")

Jack = Dog("Jack", 2)
print(Jack.name)
print(Jack.age)
Jack.walk()