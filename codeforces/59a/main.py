"""
    Time    O(N)    108 ms
    Space   O(1)    19700 KB
"""


def f():
    s = input()
    n = len(s)
    lowers = 0
    uppers = 0
    for c in s:
        if 0 <= ord(c) - ord('A') <= 25:
            uppers += 1
        elif 0 <= ord(c) - ord('a') <= 25:
            lowers += 1
    if lowers * 2 >= n:
        return s.lower()
    return s.upper()


print(f())
