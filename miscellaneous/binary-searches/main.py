def bsearch(nums, target):
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right)//2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    # to find number that <= target
    # return right

    # to find number that >= target
    # return left
    return -1


print("--bsearch--")
print(bsearch([1, 3, 5, 7, 9], 4))   # -1
print(bsearch([1, 3, 5, 7, 9], 5))   # 2


def recursiveBsearch(nums, target):
    def f(nums, target, left, right):
        if left > right:
            return -1
        mid = (left + right)//2
        if target < nums[mid]:
            return f(nums, left, mid - 1, target)
        elif target > nums[mid]:
            return f(nums, mid + 1, right, target)
        return mid
    return f(nums, target, 0, len(nums)-1)


print("--recursiveBsearch--")
print(recursiveBsearch([1, 3, 5, 7, 9], 4))   # -1
print(recursiveBsearch([1, 3, 5, 7, 9], 5))   # 2


def bSearchNearest(nums, target):
    n = len(nums)
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right)//2
        if target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            return mid
    # bounds checking
    if right < 0:
        return 0
    if left > n-1:
        return n-1
    # compare
    if abs(target - nums[right]) <= abs(target - nums[left]):
        return right
    return left


print("--bSearchNearest--")
print(bSearchNearest([1, 3, 7, 13, 20], 4))   # 1
print(bSearchNearest([1, 3, 7, 13, 20], 5))   # 1
print(bSearchNearest([1, 3, 7, 13, 20], 6))   # 2


def lowerBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target <= nums[mid]:
            right = mid
        else:
            left = mid + 1
    return left


print("--lowerBsearch--")
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 0))   # 0
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 1))   # 0
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 4))   # 2 <- 4 is just <= 5
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 5))   # 2
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 6))   # 5 <- 6 is just <= 7
print(lowerBsearch([1, 3, 5, 5, 5, 7, 9], 10))   # 7
# consider [1, 10, 23]
#      0    |    1    |    2
# -inf -> 1 | 2 -> 10 | 11 -> 23
# Or how many numbers < k


def lowerBsearch2(arr, target):
    left = 0
    right = len(arr) - 1
    result = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if target <= arr[mid]:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


print("--lowerBsearch2--")
print(lowerBsearch2([1, 3, 5, 5, 5, 7, 9], 0))   # 0
print(lowerBsearch2([1, 3, 5, 5, 5, 7, 9], 1))   # 0
print(lowerBsearch2([1, 3, 5, 5, 5, 7, 9], 4))   # 2 <- 4 is just <= 5
print(lowerBsearch2([1, 3, 5, 5, 5, 7, 9], 5))   # 2
print(lowerBsearch2([1, 3, 5, 5, 5, 7, 9], 6))   # 5 <- 6 is just <= 7
print(lowerBsearch2([1, 3, 5, 5, 5, 7, 9], 10))   # 7


def upperBsearch(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right)//2
        if target >= nums[mid]:
            left = mid + 1
        else:
            right = mid
    return right


print("--upperBsearch--")
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 0))   # 0
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 1))   # 1
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 4))   # 2 <-
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 5))   # 5
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 6))   # 5 <-
print(upperBsearch([1, 3, 5, 5, 5, 7, 9], 10))   # 7
# consider [1, 10, 23]
#      0    |   1    |    2
# -inf -> 0 | 1 -> 9 | 10 -> 23
# Or how many numbers <= k


def upperBsearch2(arr, target):
    left = 0
    right = len(arr) - 1
    res = len(arr)
    while left <= right:
        mid = (left + right) // 2
        if target >= arr[mid]:
            left = mid + 1
        else:
            res = mid
            right = mid - 1
    return res


print("--upperBsearch2--")
print(upperBsearch2([1, 3, 5, 5, 5, 7, 9], 0))   # 0
print(upperBsearch2([1, 3, 5, 5, 5, 7, 9], 1))   # 1
print(upperBsearch2([1, 3, 5, 5, 5, 7, 9], 4))   # 2 <-
print(upperBsearch2([1, 3, 5, 5, 5, 7, 9], 5))   # 5
print(upperBsearch2([1, 3, 5, 5, 5, 7, 9], 6))   # 5 <-
print(upperBsearch2([1, 3, 5, 5, 5, 7, 9], 10))   # 7


def descending_bsearch(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if target < nums[mid]:
            # right = mid - 1
            left = mid + 1
        elif target > nums[mid]:
            # left = mid + 1
            right = mid - 1
        else:
            return mid
    # to find number that <= target
    # return right

    # to find number that no >= target
    # return left

    return -1


print("--descending_bsearch--")
print(descending_bsearch([11, 9, 7, 5, 3, 1], 4))   # -1
print(descending_bsearch([11, 9, 7, 5, 3, 1], 5))   # 2
print(descending_bsearch([11, 9, 7, 5, 3, 1], 7))   # 1


def descending_lowerBsearch(nums, target):
    left = 0
    right = len(nums)-1
    res = -1
    while left <= right:
        mid = (left + right)//2
        if target <= nums[mid]:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res


print("--descending_lowerBsearch--")
print(descending_lowerBsearch([9, 7, 5, 5, 5, 3, 1], 0))   # 6
print(descending_lowerBsearch([9, 7, 5, 5, 5, 3, 1], 1))   # 5
print(descending_lowerBsearch([9, 7, 5, 5, 5, 3, 1], 4))   # 4 <-
print(descending_lowerBsearch([9, 7, 5, 5, 5, 3, 1], 5))   # 4 <-
print(descending_lowerBsearch([9, 7, 5, 5, 5, 3, 1], 10))   # -1


def descending_upperBsearch(nums, target):
    left = 0
    right = len(nums)-1
    res = -1
    while left <= right:
        mid = (left + right)//2
        if target >= nums[mid]:
            right = mid - 1
        else:
            res = mid
            left = mid + 1
    return res


print("--descending_lowerBsearch--")
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 0))   # 6
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 1))   # 5
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 4))   # 4 <-
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 5))   # 1 <-
print(descending_upperBsearch([9, 7, 5, 5, 5, 3, 1], 10))   # -1
