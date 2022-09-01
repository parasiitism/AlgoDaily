"""
    Given an array, return the starting index(L) and ending index(R) of the longest non-decreasing subarray. Where L <= R
    
    note: if there are multiple, return any one of them

    e.g.1
    Input:
        [99, 100, 1, 1, 2, 3] 
    Output:
        [2, 5]
    Explanation:
        There are at least 2 non-decreasing subarrays where L < R
        [99, 100]
        [1, 1, 2, 3] <- this is the longest
    
    e.g.2
    Input:
        [1, 1, 2, 2] 
    Output:
        [0, 3]
    Explanation:
        There are at least 3 non-decreasing subarrays where L < R
        [1, 1]
        [2, 2]
        [1, 1, 2, 2] <- the whole array is the longest

    Time    O(N)
    Space   O(N)
"""


def f(nums):
    n = len(nums)
    dp = n * [1]  # store the length at every idx
    for i in range(1, n):
        if nums[i-1] <= nums[i]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    max_length = 0
    L, R = -1, -1
    for i in range(n):
        length = dp[i]
        if length > max_length:
            max_length = length
            L = i - length + 1
            R = i
    return (L, R)


print(f([99, 100, 1, 1, 2, 3]))     # [2, 5]
print(f([1, 1, 2, 2]))              # [0, 3]
