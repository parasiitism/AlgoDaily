from collections import *


def f():
    _ = input()
    A = [int(s) for s in input().split(" ")]
    B = [int(s) for s in input().split(" ")]
    C = [int(s) for s in input().split(" ")]

    a = Counter(A)
    b = Counter(B)
    c = Counter(C)

    first = None
    for key in a:
        if key not in b or a[key]-1 == b[key]:
            first = key
            break

    second = None
    for key in b:
        if key not in c or b[key]-1 == c[key]:
            second = key

    print(first)
    print(second)


f()
