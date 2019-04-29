"""
    Given an array, find the subarrays whose elements sum to zero
"""


class Solution(object):
    def subarraySum(self, nums):
        """
        :type nums: List[int]
        :type k: int <- i made it generic that you to target any other numbers as well
        :rtype: [[]]

        https://www.youtube.com/watch?v=hLcYp67wCcM

        generic approach
        - this question is fucking similar to leetcode 325, 560
        - find loops <==============================================================
        - the basic idea is to store the previous sum in a hashtable
            e.g. key: previous sum, value: number of occurence of a previous sum
            - if currentSum - target in the hastable, the result+1

        Time	O(n)
        Space   O(n)
        7mar2019
        """
        res = []
        acc = 0
        # { key: value }
        # key: previous sum
        # value: array of indeces which previous sum equals to 0
        ht = {}
        for i in range(len(nums)):
            acc += nums[i]
            # if acc == 0, it is one of the target subarray
            if acc == 0:
                res.append(nums[:i+1])
            # if acc is in hashtbale, there is a loop
            # so there is at least one subarray
            if acc in ht:
                for j in range(len(ht[acc])):
                    idx = ht[acc][j]
                    res.append(nums[idx+1:i+1])
            # put the acc into the hashtable with index
            # such that we can do slicig later when we found a zero sum asubarray
            if acc not in ht:
                ht[acc] = [i]
            else:
                ht[acc].append(i)
        return res


# [[-1, 5, -2]]
print(Solution().subarraySum([1, 2, -5, 1, 2, -1]))

print("-----")

""" 
    folloup:
    Given an array, find the subarrays whose elements sum to k
"""


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int <- i made it generic that you to target any other numbers as well
        :rtype: [[]]

        https://www.youtube.com/watch?v=hLcYp67wCcM

        generic approach
        - this question is fucking similar to leetcode 325, 560
        - the basic idea is to store the previous sum in a hashtable
            e.g. key: previous sum, value: number of occurence of a previous sum
            - if currentSum - target in the hastable, the result+1

        Time	O(n)
        Space   O(n)
        7mar2019
        """
        res = []
        acc = 0
        # { key: value }
        # key: previous sum
        # value: array of indeces which previous sum equals to k
        ht = {}
        for i in range(len(nums)):
            acc += nums[i]
            # if acc == k, it is one of the target subarray
            if acc == k:
                res.append(nums[:i+1])
            # if acc-k == k, it is one of the target subarray
            if acc-k in ht:
                for j in range(len(ht[acc-k])):
                    idx = ht[acc-k][j]
                    res.append(nums[idx+1:i+1])
            # put the acc into the hashtable
            if acc not in ht:
                ht[acc] = [i]
            else:
                ht[acc].append(i)
        return res


# [[-1, 5, -2]]
print(Solution().subarraySum([1, -1, 5, -2, 3], 2))
# [[1, -1, 5, -2], [5, -2], [3]]
print(Solution().subarraySum([1, -1, 5, -2, 3], 3))
# [[-1, 5]]
print(Solution().subarraySum([1, -1, 5, -2, 3], 4))
# [[99]]
print(Solution().subarraySum([1, -1, 5, -2, 99], 99))
