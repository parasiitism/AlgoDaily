"""
    A hit means the requested page is already existing in the cache 
    and a miss means the requested page is not found in the cache
"""


def countMiss(nums, k):
    """
        1st approach:
        - just use an array to store the cached values

        Time    O(n^2)
        Space   O(n)
    """
    cache = []
    count = 0
    for num in nums:
        targetIdx = indexOf(cache, num)
        if targetIdx > -1:
            cache.pop(targetIdx)
        else:
            count += 1
            if k == len(cache):
                cache.pop(0)
        cache.append(num)
    return count


def indexOf(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


print(countMiss([1, 2, 3, 4, 5, 4, 1], 4))
print(countMiss([1, 2, 3, 4, 5, 4, 3, 2, 5, 6], 3))
