"""
    Given N, find the number of positive fancy numbers less than N.

    A positive integer is "fancy" if its representation in base4 only includes 0s and 1s

    e.g. 
    17 is fancy, because "101" only includes 0s and 1s
    18 is not fancy, because "102" includes 
    
    Time    O(NlogN)
    Space   O(1)
"""


def f(n):
    res = 0
    for i in range(n):
        res += isFancy(i)
    return res


def isFancy(n):
    if n == 0:
        return False
    while n > 0:
        d = n % 4
        if d > 1:
            return False
        n //= 4
    return True


print(f(1))
print(f(10))
