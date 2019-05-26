import sys


def largestRange(nums):
    nums = sorted(nums)
    print(nums)
    res = []
    cur = []
    for i in range(1, len(nums)):
        if nums[i-1]+1 == nums[i]:
            if len(cur) == 0:
                cur.append(nums[i-1])
            cur.append(nums[i])
            if len(cur) > len(res):
                res = cur
        else:
            cur = []
    return res


# [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 15]
print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))

print("-----")


def largestRange(nums):
    hs = set()
    minVal = sys.maxsize
    maxVal = -sys.maxsize
    for num in nums:
        hs.add(num)
        minVal = min(minVal, num)
        maxVal = max(maxVal, num)

    res = []
    cur = []
    for i in range(minVal, maxVal+1):
        if i in hs:
            cur.append(i)
            if len(cur) > len(res):
                res = cur
        else:
            cur = []
    return res


# [0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 15]
print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
