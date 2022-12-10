"""
    bruteforce with hashtable

    Time    O(N^2) 592 ms	
    Space   O(N^2) 8000 KB
    
"""


def f():
    T = int(input())
    for _ in range(T):
        _n = int(input())
        arr = [int(c) for c in input().split()]
        print(solve(arr))


def solve(arr):
    conseq_sums = set()
    n = len(arr)
    for i in range(n):
        pfs = 0
        for j in range(i, n):
            pfs += arr[j]
            if pfs > 8000:
                break
            if j - i >= 1:
                conseq_sums.add(pfs)
    res = 0
    for i in range(n):
        if arr[i] in conseq_sums:
            res += 1
    return res


# a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(solve(a))

# a = [1, 1, 2]
# print(solve(a))

# a = [1, 1, 1, 1, 1]
# print(solve(a))

# a = [8, 7, 6, 5, 4, 3, 2, 1]
# print(solve(a))

# a = [1]
# print(solve(a))

f()
