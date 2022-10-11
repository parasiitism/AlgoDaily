"""
    Dynamic Programming: Kadane's
    - rephrase: find the maximum # of zero-subarray
    - think if we see a zero, we get +1 point; see a 1, we get -1 point
    - then we can find out the maximum # of 0 we can flip (and consider the 1s that we flipped so we -1 point)
    - then the result is the total number 1 in the while array + the maximum zero-subarray

    Time    O(N)
    Space   O(N)
"""


def f():
    n = int(input())
    nums = [int(x) for x in input().split()]
    gains = n * [0]
    for i in range(n):
        if nums[i] == 0:
            gains[i] = 1
        else:
            gains[i] = -1
    res = -(2**32)
    cur = -(2**32)
    for i in range(n):
        x = gains[i]
        cur = max(cur+x, x)
        res = max(res, cur)
    print(sum(nums) + res)


f()
