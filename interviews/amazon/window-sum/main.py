"""
Window Sum
there are 2 versions
1. return the sum e.g. [1,2,3,4,5,6.7], k=3 => [6, 9, 12, 15, 18]
2. return the subarry e.g. [1,2,3,4,5,6.7], k=3 => [[1,2,3], [2,3,4], [3,4,5], [4,5,6], [5,6,7]]
"""


def windowSum1(nums, k):
    """
    naive approach
    - brute force O(n^2)

    1st approach
    - using the prefix sum technique
    Time    O(n)
    Space   O(k)
    29jan2019
    """
    if len(nums) == 0 or k <= 0 or k > len(nums):
        return []
    res = []
    acc = 0
    for i in range(k):
        acc += nums[i]
    res.append(acc)
    for i in range(k, len(nums)):
        acc += nums[i]
        acc -= nums[i-k]
        res.append(acc)
    return res


print(windowSum1([], 3))
print(windowSum1([1, 2, 3, 4, 5, 6, 7], -1))
print(windowSum1([1, 2, 3, 4, 5, 6, 7], 8))
print(windowSum1([1, 2, 3, 4, 5, 6, 7], 3))


def windowSum2(nums, k):
    """
    naive approach
    - brute force O(n^2)

    1st approach
    - using the prefix sum technique
    Time    O(n)
    Space   O(k)
    29jan2019
    """
    if len(nums) == 0 or k <= 0 or k > len(nums):
        return 0
    res = []

    # first item
    temp = []
    for i in range(k):
        temp.append(nums[i])
    res.append(temp)

    # 2nd item -> end
    for i in range(k, len(nums)):
        clone = res[-1][:]
        clone = clone[1:]
        clone.append(nums[i])
        # append to res
        res.append(clone)
    return res


print(windowSum2([], 3))
print(windowSum2([1, 2, 3, 4, 5, 6, 7], -1))
print(windowSum2([1, 2, 3, 4, 5, 6, 7], 8))
print(windowSum2([1, 2, 3, 4, 5, 6, 7], 3))
