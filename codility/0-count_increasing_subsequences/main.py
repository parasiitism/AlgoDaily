"""
    https://github.com/htoma/codility/blob/master/codility/Code/CountIncreasingSubsequences.cs

    Time    O(n)
    Space   O(1)
"""


def f(nums):
    res = 0
    count = 0
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
            res += count
        else:
            count = 0
    return res


# 6
a = [1, 2, 3, 4]
print(f(a))

# 0
a = [4, 3, 2, 1]
print(f(a))

# 1
a = [1, 4, 3]
print(f(a))

# 2
a = [1, 2, 2, 4]
print(f(a))

# 9
a = [1, 2, 3, 4, 2, 3, 5]
print(f(a))
