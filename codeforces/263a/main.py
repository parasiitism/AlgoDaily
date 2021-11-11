"""
    Time    O(N)    108 ms
    Space   O(1)    19700 KB
"""


def f():
    i = 0
    for _ in range(5):
        row = [int(s) for s in input().split(" ")]
        for j in range(len(row)):
            if row[j] == 1:
                return abs(i-2) + abs(j-2)
        i += 1


print(f())
