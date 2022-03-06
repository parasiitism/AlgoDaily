"""
    1st: array

    Time    O(RC)
    Space   O(RC)
    54 ms, faster than 60.00%
"""


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        left, top, right, down = s[0], int(s[1]), s[3], int(s[4])
        fromCol = ord(left) - ord('A')
        toCol = ord(right) - ord('A')
        res = []
        alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for col in range(fromCol, toCol+1):
            for row in range(top, down+1):
                a = alphabets[col]
                b = str(row)
                res.append(a+b)
        return res
