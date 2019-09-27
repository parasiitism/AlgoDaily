"""
    1st: sort

    Time    O(nlogn)
    Space   O(1)
    32 ms, faster than 76.36%
"""


class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr = sorted(arr)
        total = 0
        count = 0
        for x in arr:
            if total + x <= 5000:
                total += x
                count += 1
            else:
                break
        return count
