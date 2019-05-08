import sys

def secondLargest(nums):
    largest = -sys.maxsize
    seclargest = -sys.maxsize
    for i in range(len(nums)):
        idx = cmptr(nums, i-1, i)
        if nums[idx] > largest:
            seclargest = largest
            largest = nums[idx]
        elif nums[idx] > seclargest and nums[idx] != largest:
            seclargest = nums[idx]
    return seclargest


def cmptr(nums, i, j):
    if nums[i] > nums[j]:
        return i
    return j


a = [4, 5, 7, 6, 1, 2, 3]
print(secondLargest(a))
