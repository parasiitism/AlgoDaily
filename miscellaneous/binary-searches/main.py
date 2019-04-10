def bsearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)/2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    # to find number that no larger than target
    # return right

    # to find number that no smaller than target
    # return left

    return -1


def bSearchNearest(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)/2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    # checking
    if right < 0:
        return 0
    if left > len(nums)-1:
        return len(nums)-1
    # compare
    if abs(target-nums[right]) < abs(target-nums[left]):
        return right
    return left


def lowerBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)/2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left


def upperBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)/2
        if target >= nums[mid]:
            left = mid + 1
        else:
            right = mid
    return right
