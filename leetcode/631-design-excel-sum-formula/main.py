from collections import *

"""
    1st: brute force
    - since the dataset is small
    - store a formula to a cell, so when we sum() or get(), we calculate the sum recursively if necessary
    - so need an extra function to calculate()

    Time of get()   O(N * RC) ?
    Time of sum()   O(N * RC) ?
    47 ms, faster than 45.90%
"""


class Excel:

    def __init__(self, height: int, width: str):
        self.H = height
        self.W = self._getCol(width) + 1
        self.mat = [self.W*[0] for _ in range(self.H)]

    def set(self, row: int, column: str, val: int) -> None:
        r = self._getRow(row)
        c = self._getCol(column)
        if r >= self.H or c >= self.W:
            return
        self.mat[r][c] = val

    def get(self, row: int, column: str) -> int:
        r = self._getRow(row)
        c = self._getCol(column)
        if r >= self.H or c >= self.W:
            return 0
        v = self.mat[r][c]
        if type(v) is int:
            return v
        return self.calculate(v)

    def sum(self, row: int, column: str, strs: List[str]) -> int:
        r = self._getRow(row)
        c = self._getCol(column)
        if r >= self.H or c >= self.W:
            return 0
        self.mat[r][c] = strs
        return self.calculate(strs)

    def calculate(self, strs):
        total = 0
        for s in strs:
            colRow = s.split(':')
            if len(colRow) == 1:
                r, c = self._str2rc(colRow[0])
                val = self.mat[r][c]
                if type(val) == int:
                    total += val
                else:
                    total += self.calculate(val)
            elif len(colRow) == 2:
                top, left = self._str2rc(colRow[0])
                bottom, right = self._str2rc(colRow[1])
                for i in range(top, bottom+1):
                    for j in range(left, right+1):
                        val = self.mat[i][j]
                        if type(val) == int:
                            total += val
                        else:
                            total += self.calculate(val)
        return total

    def _getRow(self, x):
        return int(x) - 1

    def _getCol(self, c):
        return ord(c) - ord('A')

    def _str2rc(self, s):
        c = s[0]
        r = s[1:]
        c = self._getCol(c)
        r = self._getRow(r)
        return (r, c)

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
