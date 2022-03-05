from collections import *


def f():
    cntr = Counter()
    n = int(input())
    for _ in range(n):
        key = input()
        if key not in cntr:
            cntr[key] = 1
            print('OK')
        else:
            print(key + str(cntr[key]))
            cntr[key] += 1


f()
