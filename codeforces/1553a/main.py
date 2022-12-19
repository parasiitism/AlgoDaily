"""
    math
    - to fulfill the formula S(X+1) < S(X), these are the numbers 9, 19, 29, 39,....199, 299,.... 
"""


def f():
    T = int(input())
    for _ in range(T):
        n = int(input())
        print((n + 1) // 10)


f()
