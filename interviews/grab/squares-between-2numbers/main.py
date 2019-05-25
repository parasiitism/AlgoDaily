import math

"""
    1st approach:
    Find the count of all perfect squares between two numbers a and b
"""


def squareBtw(a, b):
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    a, b = min(a, b), max(a, b)
    left = int(math.ceil(math.sqrt(a)))
    right = int(math.sqrt(b))
    res = []
    for i in range(left, right+1):
        res.append(i*i)
    return res


print(squareBtw(-10, 100))
print(squareBtw(10, -100))
print(squareBtw(-10, -100))
print(squareBtw(-100, 10))

print(squareBtw(10, 100))
print(squareBtw(10, 100))
print(squareBtw(100, 1000))
print(squareBtw(1000, 100))

print("-----")

"""
    2nd approach:
    Find the count of all perfect squares between two numbers a and b
"""


def squareBtw(a, b):
    if a < 0:
        a = 0
    if b < 0:
        b = 0
    a, b = min(a, b), max(a, b)
    root = int(math.sqrt(a))
    cur = root
    res = []
    while cur * cur <= b:
        if cur * cur >= a:
            res.append(cur*cur)
        cur += 1
    return res


print(squareBtw(-10, 100))
print(squareBtw(10, -100))
print(squareBtw(-10, -100))
print(squareBtw(-100, 10))

print(squareBtw(10, 100))
print(squareBtw(10, 100))
print(squareBtw(100, 1000))
print(squareBtw(1000, 100))
