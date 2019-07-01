"""
    1st approach: binary search, learned from others
    - the easiest is to use hashset like first missing positve. but if the numbers are sparsely separated, it gets LTE because it takes O(n)
    - a better way is to use binary search to search the range "accumulative counts of missing items" between numbers

    e.g.1
    nums = [4, 8, 11, 13]
    cnts = [0, 3,  5,  6] <- from 4 to 8, 3 numbers are missing. from 8 to 11, 2 numbers are missing...etc

    then we can do lower bound binary search, lets say k=4
    nums = [4, 8, 11, 13]
    cnts = [0, 3,  5,  6]
                   ^
                   there are 5 missing numbers before nums[2]
                    , so the result must be between nums[1] and nums[2]
    
    result = nums[1] + (k-cnts[1]) = 8 + (4-3) = 9

    e.g.2 what if k = 10?
    nums = [4, 8, 11, 13]
    cnts = [0, 3,  5,  6]

    after we did binary search, left = 4, 
    it means our result mnust be larger than the upper bound of numbers, nums[-1] = 13
    
    we just have to subtract the k with number of missing numbers between bounds to get the diff from nums[-1], 
    so result = nums[-1] + k - counts[-1] = 13 + 10 - 6 = 17

    ref:
    - https://leetcode.com/problems/missing-element-in-sorted-array/solution/

    Time    O(logn)
    Space   O(n)
    304 ms, faster than 19.61%
"""


class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counts = len(nums) * [0]
        for i in range(1, len(nums)):
            counts[i] = counts[i-1] + nums[i] - nums[i-1] - 1
        # binary serach
        left = 0
        right = len(counts)
        while left < right:
            mid = (left + right)//2
            if k <= counts[mid]:
                right = mid
            else:
                left = mid + 1
        # if exceed the boundary
        if left == len(counts):
            return nums[-1] - counts[-1] + k
        # if not
        btw = k - counts[left-1]
        return nums[left-1] + btw


# 9
a = [4, 8, 11, 13]
b = 4
print(Solution().missingElement(a, b))

# 17
a = [4, 8, 11, 13]
b = 10
print(Solution().missingElement(a, b))
