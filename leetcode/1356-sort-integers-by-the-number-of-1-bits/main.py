"""
    1st: bit op + sort
    1. count the number of bits for each number from input
    2. sort the input

    Time    O(NlogN * logN)
    Space   O(1)
    424 ms, faster than 5.26%
"""


class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def f(num):
            count = 0
            while num > 0:
                if num & 1 > 0:
                    count += 1
                num >>= 1
            return count

        def cmpter(a, b):
            if f(a) == f(b):
                return a - b
            return f(a) - f(b)

        return sorted(arr, cmp=cmpter)
