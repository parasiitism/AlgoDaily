"""
    binary search

    Time    O(81 + 81log81 + Tlog81)
    Space   O(N)
"""


def f():
    A = []
    for i in range(1, 10):
        for j in range(1, 10):
            s = j * str(i)
            A.append(int(s))
    A.sort()
    t = int(input())
    for _ in range(t):
        n = int(input())
        j = upperBsearch(A, n)
        print(j)


def upperBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target >= nums[mid]:
            left = mid + 1
        else:
            right = mid
    return right


f()
