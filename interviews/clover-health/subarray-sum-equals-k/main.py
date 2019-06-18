"""
It is basically a variation of lc560: Subarray Sum Equals K

Given a sequence of positive integers A[] and an integer T, return whether there is a continuous sequence in A[] that sums up to exactly T.

Input: An integer array containing positive integers
Output: If has solution, the subarray of A[] that sums up to exactly T, if no solution, return an empty array

*Example 1:*
Input:  [23, 5, 4, 7, 2, 11] & 20
Output: [7, 2, 11]

*Example 2:*
Input: [1, 3, 5, 23, 2] & 8 
Output: [3, 5]

*Example 3:*
Input: [1, 3, 5, 23, 2] & 7
Output: []

O(n^2)
# cursum 

[1, 3, 5, 23, 2] & 8
1   4   9   
    3   8
        5

target = 3+5+23+2

O(n) Space(n)
[1, 3, 5, 23, 2] & 8
1   4  9   32  34
we see that 9-1 = 8, so nums[1:3] is the answer

"""


def rangeSum2Target(nums, target):
    pfs = 0
    m = {}
    for i in range(len(nums)):
        pfs += nums[i]
        # from index 0
        if pfs == target:
            return nums[:i+1]
        # find if the remain is in the hashtable
        if pfs - target in m:
            idx = m[pfs-target][0]
            return nums[idx+1:i+1]
        if pfs not in m:
            m[pfs] = [i]
        else:
            m[pfs].append(i)
    return []


a = [1, 3, 5, 23, 2]
b = 7
print(rangeSum2Target(a, b))
b = 8
print(rangeSum2Target(a, b))
b = 25
print(rangeSum2Target(a, b))

print("-----")

a = [1, 3, 5, 23, 2, 1, 3, 2]
b = 6
print(rangeSum2Target(a, b))
