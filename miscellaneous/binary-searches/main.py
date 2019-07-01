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
    # to find number that <= target
    # return right

    # to find number that no >= target
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


print("--lowerBsearch--")
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 4))   # 2
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 5))   # 2


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


print("--upperBsearch--")
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 5))   # 5
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 6))   # 5
