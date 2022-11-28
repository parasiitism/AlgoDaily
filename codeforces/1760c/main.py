"""
    Array trick: O(N) to find the 1st and 2nd largest

    Time    O(N)
    Space   O(1)
"""


def f():
    T = int(input())
    for _ in range(T):
        _ = input()
        nums = [int(c) for c in input().split()]
        solve(nums)


def solve(nums):
    largest1, largest2 = firstAndSecondLargest(nums)
    res = []
    for x in nums:
        if x != largest1:
            res.append(x - largest1)
        else:
            res.append(x - largest2)
    print(" ".join([str(x) for x in res]))


def firstAndSecondLargest(nums):
    largest1 = -2**32
    largest2 = -2**32
    for x in nums:
        if x > largest1:
            largest2 = largest1
            largest1 = x
        elif largest2 < x:
            largest2 = x
    if largest2 == -2**32:
        largest2 = largest1
    return largest1, largest2


# print(firstAndSecondLargest([5, 5]))
# print(firstAndSecondLargest([5, 7, 3, 6, 7, 3, 4]))

f()
