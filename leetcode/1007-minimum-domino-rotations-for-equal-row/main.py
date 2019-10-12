import sys

"""
    1st: unknown
    - actaully i am not sure what type it belongs to, i use hashtable just for counting
    
    e.g.
    A = [2,1,2,4,2,2]
    B = [5,2,6,2,3,2]

    possibility 1: 2 swaps
    [2,2,2,2,2,2]
    [5,1,6,4,3,2]

    possibility 2: 3 swaps
    [5,1,6,4,3,2]
    [2,2,2,2,2,2]

    the number of swap to make either one of the list single value is 2 or 3, return 2 because 2 is smaller

    Time    O(kN)
    Space   O(N)
    1124 ms, faster than 47.44%
"""


class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        counts = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        for x in A:
            counts[x] += 1
        for y in B:
            counts[y] += 1

        res = sys.maxsize
        for key in counts:
            if counts[key] >= len(A):
                c1, i1 = self.a2b(A, B, key)
                c2, i2 = self.a2b(B, A, key)
                if i1 == len(A):
                    res = min(res, c1)
                if i2 == len(A):
                    res = min(res, c2)
        if res == sys.maxsize:
            return -1
        return res

    def a2b(self, A, B, key):
        count = 0
        i = 0
        while i < len(A):
            if A[i] == key:
                i += 1
            elif B[i] == key:
                i += 1
                count += 1
            else:
                break
        return count, i
