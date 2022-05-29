"""
    sort + binary search

    Time    O(AlogB)
    Space   O(A+B)
"""


def f():
    _ = int(input())
    A = [int(x) for x in input().split()]
    _ = int(input())
    B = [int(x) for x in input().split()]
    A.sort()
    B.sort()

    shorter, longer = [], []
    if len(A) <= len(B):
        shorter = A
        longer = B
    else:
        shorter = B
        longer = A

    res = 0
    for i in range(len(shorter)):
        a = shorter[i]
        j = lowerBsearch(longer, a-1)
        if j == len(longer):
            j -= 1
        if 0 <= j < len(longer) and abs(longer[j] - a) <= 1:
            res += 1
            longer.pop(j)
    return res


def lowerBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left


print(f())
"""
4
4 5 4 4
5
5 3 4 2 4

4 4 4 5
2 3 4 4 5
"""
