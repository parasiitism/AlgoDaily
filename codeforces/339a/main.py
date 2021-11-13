"""
    - similar to leetcode75
"""


def f():
    nums = [int(s) for s in input().split("+")]
    n = len(nums)
    left = 0
    mid = 0
    right = n - 1
    while mid <= right:
        if nums[mid] == 1:
            nums[mid], nums[left] = nums[left], nums[mid]
            left += 1
            mid += 1
        elif nums[mid] == 3:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
        else:
            mid += 1
    res = ''
    for i in range(n):
        res += str(nums[i])
        if i < n-1:
            res += '+'
    return res


print(f())
