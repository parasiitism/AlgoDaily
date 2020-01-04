"""
    1st: math
    
    Time    O(N/2)
    Space   O(N)
    24 ms, faster than 42.69%
"""


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        arr = []
        for i in range(1, 1 + n//2):
            arr.append(-i)
            arr.append(i)
        if n % 2 == 0:
            return arr
        return arr + [0]
