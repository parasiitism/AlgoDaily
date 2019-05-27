"""
    1st approach: zero sum subarray

    - this question is fucking similar to leetcode 325, 560, 930
    - the general idea is transform 0 to -1, do prefix sum
    - if 2 cases:
        1. current prefix sum == 0, nums[:i+1] is a zero sum subarray
        2. if found this prefix sum from the hashtable, it means that there is a loop which we have 0 zero gain

    ref:
    - https://www.youtube.com/watch?v=hLcYp67wCcM

    Time	O(n)
    Space   O(n)
    1may2019
"""


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = []
        for num in nums:
            if num == 0:
                arr.append(-1)
            else:
                arr.append(1)
        m = {}
        total = 0
        res = 0
        for i in range(len(arr)):
            total += arr[i]

            if total == 0:
                res = max(res, i+1)

            if total in m:
                leftMostIdx = m[total][0]
                diff = i - leftMostIdx
                res = max(res, diff)

            if total not in m:
                m[total] = [i]
            else:
                m[total].append(i)

        return res
