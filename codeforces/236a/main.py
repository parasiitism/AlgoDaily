"""
    Time    O(N)    108 ms
    Space   O(1)    19700 KB
"""


def f():
    s = input()
    hs = set()
    for c in s:
        hs.add(c)
    if len(hs) % 2 == 0:
        return "CHAT WITH HER!"
    return "IGNORE HIM!"


print(f())
