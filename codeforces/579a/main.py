"""
    it is actually ask how many ones in the BIT representation
"""


def f():
    n = int(input())
    res = 0
    while n > 0:
        res += n % 2
        n //= 2
    return res


print(f())
