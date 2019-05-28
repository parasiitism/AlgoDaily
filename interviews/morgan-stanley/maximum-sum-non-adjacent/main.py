"""
    Find maximum sum for non adjacent elements.
    Variation is finding maximum sum non adjacent elements assuming its a circular array.
    So first element cannot be with last element
    
    Time complexity O(n)
    Space complexity O(1)

    ref:
    - https://www.youtube.com/watch?v=UtGtF6nc35g

    O(n)
"""


def maxSumForNonAdjacent(nums):
    if len(nums) == 0:
        return 0
    included = nums[0]
    excluded = 0
    for i in range(1, len(nums)):
        temp = included
        included = max(excluded+nums[i], included)
        excluded = temp
    # return included
    return max(included, excluded)


# 4, 4, 1 => 9
print(maxSumForNonAdjacent([4, 1, 1, 4, 2, 1]))

# 5, 5, 10, 100, 10, 5 => 110
print(maxSumForNonAdjacent([5, 5, 10, 100, 10, 5]))
