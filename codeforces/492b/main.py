from math import ceil


def f():
    n, L = map(int, input().split())
    if n == 0:
        return -1
    nums = [int(s) for s in input().split(" ")]
    nums = sorted(list(set(nums)))
    max_diff = 0
    for i in range(1, len(nums)):
        max_diff = max(max_diff, (nums[i] - nums[i-1])/2)
    max_diff = max(max_diff, nums[0] - 0)
    max_diff = max(max_diff, L - nums[-1])
    return max_diff


print(f())
