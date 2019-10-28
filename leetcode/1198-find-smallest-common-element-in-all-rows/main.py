"""
    1st: brute force with hashtbale

    Time    O(RC)
    Space   O(C)
    472 ms, faster than 60.33%
"""
class Solution(object):
    def smallestCommonElement(self, matrix):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        hs = set(matrix[0])
        for arr in matrix:
            existed = []
            for x in arr:
                if x in hs:
                    existed.append(x)
            if len(existed) == 0:
                return -1
            hs = set(existed)
        return sorted(hs)[0]