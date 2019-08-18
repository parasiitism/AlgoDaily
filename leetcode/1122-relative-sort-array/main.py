"""
    1st approach: hashtable
    
    Time    O(A1 + A2 + A2 + O(NlogN))
    Space   O(A1+A2)
    20ms beats 90.55%
"""


class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        m = {}
        for x in arr2:
            m[x] = 0
        excluded = []
        for x in arr1:
            if x in m:
                m[x] += 1
            else:
                excluded.append(x)
        result = []
        for x in arr2:
            result += m[x] * [x]
        result += sorted(excluded)
        return result
