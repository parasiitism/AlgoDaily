"""
    1st: binary search
    - since the input function is an increasing function
    - we can use binary search to look for the proper counterpart

    Time    O(NlogN)
    Space   O(1)
    184 ms, faster than 22.97%
"""


class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, 1001):
            j = self.bsearch(customfunction.f, i, z)
            if j != -1:
                res.append([i, j])
        return res

    def bsearch(self, f, i, target):
        left = 1
        right = 1000
        while left <= right:
            mid = (left + right)/2
            temp = f(i, mid)
            if target < temp:
                right = mid - 1
            elif target > temp:
                left = mid + 1
            else:
                return mid
        return -1
