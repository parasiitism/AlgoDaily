"""
  Write a function to return an array such that
  f(nums) = abs(nums[0]-nums[1]) + abs(nums[1]-nums[2]) + abs(nums[2]-nums[3]) will be largest
"""


def fourIntegers(a, b, c, d):
    """
      e.g.    3,4,5,6
      step1:  4,3,6,5
      step2:  5,3,6,4
    """
    nums = [a, b, c, d]
    nums = sorted(nums)
    return [nums[2], nums[0], nums[3], nums[1]]


print(fourIntegers(3, 4, 5, 6))
