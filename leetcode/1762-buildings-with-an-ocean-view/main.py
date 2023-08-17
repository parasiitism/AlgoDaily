"""
    1st: easy dp
    - keep the peak when we traverse the list from the ocean
    - put the index of a higher building along the way
    - similar to lc121

    Time    O(N)
    Space   O(N)
    608 ms, faster than 100.00%
"""


class Solution:
    def findBuildings(self, A: List[int]) -> List[int]:
        peak = -1
        res = []
        for i in range(len(A)-1, -1, -1):
            if A[i] > peak:
                peak = A[i]
                res.append(i)
        return res[::-1]
