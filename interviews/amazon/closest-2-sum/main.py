"""
  Given an array nums of n integers, 
  find two integers in nums such that the sum is closest(<=) to a given number, target
  
  Questions to ask:
  - will there be 2 or more pairs have the same sum?
  - the result must contains 2 items? what if [1,2,10] and 10, should i just return 10?
  - will there be no result?
  - all numbers in nums > 0?
  - maxCap > 0?
"""


def closest2sum(nums, maxCap):
    nums.sort()
    i = 0
    j = len(nums) - 1
    res = 0
    first = None
    second = None
    while i < j:
        total = nums[i]+nums[j]
        if total > res and total <= maxCap:
            first = nums[i]
            second = nums[j]
            res = total
        if total > maxCap:
            j -= 1
        else:
            i += 1
    return (first, second, res)


# normal case
nums = [2, 4, 10, 11, 6, 5, 9]
print(closest2sum(nums, 12))

nums = [2, 4, 10, 11, 6, 5, 9]
print(closest2sum(nums, 22))

# duplicate: for now i just return first one i found
nums = [2, 4, 10, 11, 6, 6, 9]
print(closest2sum(nums, 12))

# one item?
nums = [2, 4, 10, 11, 6, 6, 9]
print(closest2sum(nums, 2))

# no result
nums = [2, 4, 10, 11, 6, 6, 9]
print(closest2sum(nums, 1))
