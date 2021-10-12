
"""
    1st approach:

    Time    
    Space   
"""


def f():
    T = int(input())
    for _ in range(T):
        s = input()
        n = len(s)
        if n <= 10:
            print(s)
        else:
            print(s[0] + str(n - 2) + s[-1])


f()
