"""
    Given an array of integers, return the number of identical pairs that has the same value

    e.g. nums = [3, 5, 6, 3, 3, 5]
    The result = 4 because identical pairs, (indexA, indexB), are (0, 3), (0, 4), (1, 5) and (3, 4)
    Note that pairs (2, 2) is not counted because each item can only be used once
    Note that pairs (5, 1) is not counted because we have (1, 5) already
"""


def f(nums):
    m = {}
    for num in nums:
        if num not in m:
            m[num] = 1
        else:
            m[num] += 1
    res = 0
    for key in m:
        count = m[key]
        numOfPairs = count * (count - 1) / 2
        res += numOfPairs
    return res


a = [3, 5, 6, 3, 3, 5]
print(f(a))
