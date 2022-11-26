"""
# brute-force
# Time O(NNlogM)    LTE

def f():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = [int(c) for c in input().split()]
        print(solve(arr))


def solve(arr):
    n = len(arr)
    res = -1
    for i in range(n):
        for j in range(n):
            if find_gcd(arr[i], arr[j]) == 1:
                res = max(res, i + j)
    if res == -1:
        return res
    return res + 2


def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)


f()
"""

"""
    hashtable

    Time    O(1000*1000 log1000)
    LTE in python but AC in pypy
"""


def f():
    T = int(input())
    for _ in range(T):
        input()
        arr = [int(c) for c in input().split()]
        print(solve(arr))


def solve(arr):
    n = len(arr)
    biggests = 1001 * [-1]
    for i in range(n):
        x = arr[i]
        biggests[x] = max(biggests[x], i)
    res = -1
    for x in range(1, 1001):
        i = biggests[x]
        if i == -1:
            continue
        for y in range(1, 1001):
            j = biggests[y]
            if j == -1:
                continue
            if find_gcd(x, y) == 1:
                res = max(res, i + j)
    if res == -1:
        return res
    return res + 2


def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)


f()
