"""
    it seems like there is no other better ways
    1. split by .
    2. iterate and compare each section
    3. if compare result != 0, return immediately

    Time	O(n)
    Space	O(n)
    0ms beats 100%
    28 ms, faster than 17.48%
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        while len(arr1) > 0 or len(arr2) > 0:
            a = 0
            if len(arr1) > 0:
                a = int(arr1.pop(0))
            b = 0
            if len(arr2) > 0:
                b = int(arr2.pop(0))
            if a < b:
                return -1
            elif a > b:
                return 1
        return 0
