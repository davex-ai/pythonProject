class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        return True if self.age > other.age else False

Jack = Dog("Jack", 2)
James = Dog("James", 4)
print(James > Jack)

# Other Overloading Operators
# __add__()  responds to the + operator
# __sub__() responds to the - operator
# __mul__() responds to the * operator
# __truediv__() responds to the / operator
# __floordiv__() responds to the // operator
# __mod__() responds to the % operator
# __pow__() responds to the ** operator
# __rshift__() responds to the >> operator
# __lshift__() responds to the << operator
# __and__() responds to the & operator
# __or__() responds to the | operator
# __xor__() responds to the ^ operator