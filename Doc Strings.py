"""This file teaches docstrings
IT has comments"""
from Decorator import hello


def increment(n):
    """Increment a nuber"""
    return n+1
class Dog:
    """ A class representing a dog"""# This is a docstring
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} barks\n WOOF!!")

print(help(Dog))