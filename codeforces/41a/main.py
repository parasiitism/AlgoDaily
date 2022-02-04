

"""
    Time    O(N)
    Space   O(N)
"""


def f():
    s = input()
    t = input()
    _s = s[::-1]
    if _s == t:
        print("YES")
    else:
        print("NO")


f()
