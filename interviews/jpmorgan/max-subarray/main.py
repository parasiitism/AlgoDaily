def maxSubArray(nums):
    res = 0
    prevSum = 0
    for rawNum in nums:
        num = int(rawNum)
        prevSum = max(prevSum+num, num)
        res = max(res, prevSum)
    return res


# a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# print(Solution().maxSubArray(a))

# a = [4, 1, -5, 6, -3, 2]
# print(Solution().maxSubArray(a))

# a = [7, -3, -10, 4, 2, 8, -2, 4, -5, -6]
# print(Solution().maxSubArray(a))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
# read input to know N
t = int(input())
# read N lines
for i in range(t):
    ri = input()  # raw_input() for python2.7
    nums = ri.split()
    result = maxSubArray(nums)
    print(result)
"""
test

2
7 -3 -10 4 2 8 -2 4 -5 -6
10 7 -3 -10 4 2 8 -2 4 -5 -6
"""
