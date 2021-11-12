"""
    Time    O(N)    108 ms
    Space   O(1)    19700 KB
"""


def f():
    S = input().lower()
    T = input().lower()
    for i in range(len(S)):
        if S[i] < T[i]:
            return -1
        elif S[i] > T[i]:
            return 1
    return 0


print(f())
