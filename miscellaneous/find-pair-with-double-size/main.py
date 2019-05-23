"""
    for each number, find out its pair partner which is double in value of it

    idea: similar to 2sum
"""


def findPair(nums):
    res = []
    ht = {}
    for i in range(len(nums)):
        num = nums[i]
        if num * 2 in ht:
            res.append([i, ht[num * 2]])
        ht[num] = i
    ht = {}
    for i in range(len(nums)-1, -1, -1):
        num = nums[i]
        if num * 2 in ht:
            res.append([i, ht[num * 2]])
        ht[num] = i
    return res


print(findPair([1, 2, 5, 6, 4]))
print(findPair([4, 2, 5, 6, 1]))
