"""
    Math
    - If a number has an odd divisor, then it has an odd prime divisor
    - There is only one even prime number 2. So, if a number has no odd divisors, then it must be a power of two.
    - If a number is a power of two, then it contains only one unit in the binary notation

    Time    O(T)
"""


def f():
    T = int(input())
    for _ in range(T):
        x = int(input())
        if x & (x-1) == 0:
            print("NO")
        else:
            print("YES")


f()
