import sys


def Solution(nums):
    agg = 0
    for num in nums:
        agg += num
    avg = agg / (len(nums) * 1.0)
    res = sys.maxsize
    for num in nums:
        if abs(num - avg) < abs(res - avg):
            res = num
    return res


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2]
print(Solution(a))
