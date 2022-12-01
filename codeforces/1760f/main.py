"""
    binary search
    - https://codeforces.com/blog/entry/109348
"""


def f():
    T = int(input())
    for _ in range(T):
        _, c, d = [int(c) for c in input().split()]
        nums = [int(c) for c in input().split()]
        print(solve(nums, c, d))


def solve(nums, c, d):
    n = len(nums)
    nums.sort(key=lambda x: -x)
    L, R = 0, d + 1
    while L < R:
        k = (L + R + 1)//2
        coins = 0
        for i in range(d):
            if i % k < n:
                coins += nums[i % k]
        if coins >= c:
            L = k
        else:
            R = k - 1
    if L == 0:
        return("Impossible")
    elif L == d + 1:
        return("Infinity")
    return L - 1


# print(solve([1, 2], 5, 4))
# print(solve([100, 10], 20, 10))
# print(solve([7, 2, 6], 100, 3))
# print(solve([4, 5, 6, 7], 20, 3))
# print(solve([8217734, 927368, 26389746, 627896974], 100000000000, 2022))

f()
