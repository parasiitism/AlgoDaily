"""
    1st approach: bit op
    - get the position of each one, compare with the previous position
    - if the diff between curpos and prevpos is larger than the intermediate result, update the intermediate result

    Time    O(logn)
    Space   O(1)
    28 ms, faster than 20.35%
"""


class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        prev = -1
        i = 0
        while N > 0:
            if N & 1 == 1:
                if prev != -1:
                    diff = i - prev
                    res = max(res, diff)
                prev = i
            i += 1
            N >>= 1
        return res
