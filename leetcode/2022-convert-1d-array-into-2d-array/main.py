"""
    1st: array

    Time    O(MN)
    Space   O(MN)
    1052 ms, faster than 100.00%
"""


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = []
        row = []
        for x in original:
            row.append(x)
            if len(row) == n:
                res.append(row)
                row = []
        return res
