from collections import defaultdict
"""
    1st: binary search

    Time    O(AlogB + AlogC)
    Space   O(min(A, B, C))
    96 ms, faster than 20.00%
"""


class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        res = []
        for x in arr1:
            found1 = self.bsearch(arr2, x)
            if found1 == -1:
                continue
            found2 = self.bsearch(arr3, x)
            if found2 != -1:
                res.append(x)
        return res

    def bsearch(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right)//2
            if target == arr[mid]:
                return mid
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1


"""
    2nd: hashtable

    Time    O(A + B + C)
    Space   O(max(A, B, C))
    60 ms, faster than 94.39%
"""


class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        ht = defaultdict(int)
        for x in arr1:
            ht[x] += 1
        for x in arr2:
            ht[x] += 1
        for x in arr3:
            ht[x] += 1
        res = []
        for key in ht:
            if ht[key] == 3:
                res.append(key)
        return res
