def secondLargest(nums):
    largest = max(nums[0], nums[1])
    seclargest = min(nums[0], nums[1])
    for i in range(1, len(nums)):
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
