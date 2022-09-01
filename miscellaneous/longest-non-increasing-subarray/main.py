"""
    Given an array, return the starting index(L) and ending index(R) of the longest non-increasing subarray. Where L <= R
    
    note: if there are multiple, return any one of them

    e.g.1
    Input:
        [1, 1, 4, 4, 3, 2, 1, 5, 6, 7, 6]
    Output:
        [2, 6]
    Explanation:
        There are 3 non-increasing subarray
        [1, 1]
        [7, 6]
        [4, 4, 3, 2, 1] <- this is the longest
    
    Time    O(N)
    Space   O(N)
"""


def f(nums):
    n = len(nums)
    dp = n * [1]  # store the length at every idx
    for i in range(1, n):
        if nums[i-1] >= nums[i]:
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


print(f([1, 1, 4, 4, 3, 2, 1, 5, 6, 7, 6]))     # [2, 6]
print(f([1, 4, 3, 2, 5]))                       # [1, 3]
print(f([1, 2, 3, 4, 5]))                       # [0, 0]
print(f([1, 1, 4, 3, 2, 5]))                    # (2, 4)
print(f([1, 4, 3, 2, 5, 5]))                    # (1, 3)
print(f([1, 4, 3, 3, 2, 5]))                    # (1, 4)
