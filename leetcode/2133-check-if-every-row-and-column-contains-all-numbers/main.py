"""
    1st: hashtable
    - check every row and column

    Time    O(RC)
    Space   O(RC) <- the hashset
    764 ms, faster than 14.29%
"""


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            seen = set()
            for j in range(n):
                seen.add(matrix[i][j])
            if len(seen) != n:
                return False
        for j in range(n):
            seen = set()
            for i in range(n):
                seen.add(matrix[i][j])
            if len(seen) != n:
                return False
        return True
