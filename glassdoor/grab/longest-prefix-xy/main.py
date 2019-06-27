"""
    Given an array of N integers, 
    find the longest leading fragment of array which contains equal no. of X and Y. 
    
    Expected time complexity is O(n)
"""


def longestPrefix(nums, X, Y):
    xcount = 0
    ycount = 0
    res = ""
    for i in range(len(nums)):
        num = nums[i]
        if num == X:
            xcount += 1
        if num == Y:
            ycount += 1
        if xcount == ycount:
            res = nums[:i+1]
    return res


a = [7, 42, 5, 6, 42, 8, 7, 5, 3, 6, 7]
b = 7
c = 42
print(longestPrefix(a, b, c))
