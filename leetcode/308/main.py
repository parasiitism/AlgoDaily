"""
    Binary Index Tree
    - create BIT on each row
    - when we query, use BIT range query to fast compute the sum from col1 to col2

    Time of update()    O(logC)
    Time of sumRange()  O(RlogC)
    Runtime 280 ms Beats 82.3%
"""


class BinaryIndexedTree(object):

    def __init__(self, n):
        self.fenwickTree = (n+1) * [0]

    def update(self, i, val):
        k = i + 1
        while k < len(self.fenwickTree):
            self.fenwickTree[k] += val
            k += k & -k

    def getSum(self, i):
        s = 0
        k = i + 1
        while k > 0:
            s += self.fenwickTree[k]
            k -= k & -k
        return s

    def getRangeSum(self, i, j):
        return self.getSum(j) - self.getSum(i-1)


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.cache = []
        self.BITs = []
        for i in range(R):
            BIT = BinaryIndexedTree(C)
            row = C * [0]
            for j in range(C):
                x = matrix[i][j]
                BIT.update(j, x)
                row[j] = x
            self.BITs.append(BIT)
            self.cache.append(row)

    def update(self, row: int, col: int, val: int) -> None:
        prev = self.cache[row][col]
        diff = val - prev
        self.BITs[row].update(col, diff)
        self.cache[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2+1):
            res += self.BITs[i].getRangeSum(col1, col2)
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
