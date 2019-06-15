import sys


def maxDiff(nums):
    minVal = sys.maxsize
    maxVal = -sys.maxsize
    for c in nums:
        num = int(c)
        minVal = min(minVal, num)
        maxVal = max(maxVal, num)
    return maxVal - minVal


a = [1, 2, 10, 0, 3, 9]
print(maxDiff(a))

a = [4, -9, -3, 0, 7, 9]
print(maxDiff(a))

# input() reads a string with a line of input, stripping the ' ' (newline) at the end.
# This is all you need for most Code Jam problems.
# read input to know N
t = int(input())
# read N lines
for i in range(t):
    ri = input()  # raw_input() for python2.7
    nums = ri.split(',')
    result = maxDiff(nums)
    print(result)
