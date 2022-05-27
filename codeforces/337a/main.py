"""
    sliding window

    Time    O(N)
    Space   O(1)
"""


def f():
    n, m = map(int, input().split())
    nums = [int(s) for s in input().split()]
    nums.sort()
    res = 2**32
    for i in range(n-1, m):
        diff = nums[i] - nums[i-n+1]
        res = min(res, diff)
    return res


print(f())
