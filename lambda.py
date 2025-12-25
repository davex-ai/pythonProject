from functools import reduce

lambda num : num * 2
multiply = lambda a, b : a * b
print(multiply(2, 5))

# Map
numb = [1, 2, 3, 4, 5]
"""Normal Way"""
def double(a):
    return a * 2
print(list(map(double, numb)))
"""Lambda Way"""
print(list(map(lambda a: a * 2, numb)))

# Filter
"""Normal Way"""
def even(n):
    return n % 2 == 0
print(list(filter(even, numb)))
"""Lambda Way"""
print(list(filter(lambda n : n % 2 == 0, numb)))

# Reduce
"""Normal Way"""
expenses = [
    ('Crocs', 15000 ),
    ('Laptop', 650000 ),
    ('Headphone', 25000 ),
]
total = 0
for expenses in expenses:
    total += expenses[1]
print(total)
"""Lambda Way"""
add = reduce(lambda a, b: a[1] + b[1] , expenses)
print(add)

