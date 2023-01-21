"""
    Binary Indexed Tree

    Time of init()      O(N)
    Time of gather()    O(maxRow)
    Time of scatter()   O(logM + maxRow)
    Space               O(N)

    TLE
"""


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.used_rows = n * [0]
        self.BIT = BinaryIndexedTree(n)
        for i in range(n):
            self.BIT.update(i, m)

    def gather(self, k: int, maxRow: int) -> List[int]:
        for i in range(maxRow + 1):
            availables = self.m - self.used_rows[i]
            if availables >= k:
                first_col = self.used_rows[i]
                self.used_rows[i] += k
                self.BIT.update(i, -k)
                return [i, first_col]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        total = self.BIT.getSum(maxRow)
        if total < k:
            return False
        for i in range(maxRow + 1):
            availables = self.m - self.used_rows[i]
            if availables >= k:
                self.used_rows[i] += k
                self.BIT.update(i, -k)
                k = 0
            else:
                k -= availables
                self.used_rows[i] += availables
                self.BIT.update(i, -availables)
        return True


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
