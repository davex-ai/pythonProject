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
    ('Crocs', 15000),
    ('Laptop', 650000),
    ('Headphone', 25000),
]

# Normal sum
total = 0
for item in expenses:
    total += item[1]
print(total)  # 690000

# Lambda / reduce way
add = reduce(lambda total, item: total + item[1], expenses, 0)
print(add)  # 690000


