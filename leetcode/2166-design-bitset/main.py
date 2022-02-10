"""
    0th: brute force
    Time of flip,all,one,count,toString     O(N)
    Space                                   O(N) 
    TLE
"""


class Bitset:

    def __init__(self, size: int):
        self.digits = size * [0]

    def fix(self, idx: int) -> None:
        self.digits[idx] = 1

    def unfix(self, idx: int) -> None:
        self.digits[idx] = 0

    def flip(self) -> None:
        for i in range(len(self.digits)):
            self.digits[i] = (self.digits[i] + 1) % 2

    def all(self) -> bool:
        return sum(self.digits) == len(self.digits)

    def one(self) -> bool:
        return sum(self.digits) > 0

    def count(self) -> int:
        return sum(self.digits)

    def toString(self) -> str:
        return ''.join([str(x) for x in self.digits])


"""
    1st: hashtable

    Time of flip,all,one,count      O(1)
    Time of toString                O(N)
    Space                           O(N)
    820 ms, faster than 66.67% 
"""


class Bitset:

    def __init__(self, size: int):
        self.ones = set()
        self.zeros = set()
        self.n = size
        for i in range(size):
            self.zeros.add(i)

    def fix(self, idx: int) -> None:
        self.ones.add(idx)
        if idx in self.zeros:
            self.zeros.remove(idx)

    def unfix(self, idx: int) -> None:
        self.zeros.add(idx)
        if idx in self.ones:
            self.ones.remove(idx)

    def flip(self) -> None:
        self.zeros, self.ones = self.ones, self.zeros

    def all(self) -> bool:
        return len(self.ones) == self.n

    def one(self) -> bool:
        return len(self.ones) > 0

    def count(self) -> int:
        return len(self.ones)

    def toString(self) -> str:
        res = ''
        for i in range(self.n):
            if i in self.zeros:
                res += '0'
            else:
                res += '1'
        return res


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
