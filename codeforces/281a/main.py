
"""
    Time    O(N)
    Space   O(N)
"""


def f():
    s = input()
    first = s[0]
    return first.upper() + s[1:]


print(f())
