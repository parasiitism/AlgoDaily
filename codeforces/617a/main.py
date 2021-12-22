"""
    Math

    Time    O(1)
    Space   O(1)
"""


def f():
    x = int(input())
    a, x = x//5, x % 5
    b, x = x//4, x % 4
    c, x = x//3, x % 3
    d, x = x//2, x % 2
    return a + b + c + d + x


print(f())
