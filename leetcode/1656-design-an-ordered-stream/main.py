"""
    1st: pointer

    Time of init()      O(N)
    Time of insert()    O(N)
    Space               O(N)
    194ms beats 99.54%
"""


class OrderedStream:

    def __init__(self, n: int):
        self.ptr = 1
        self.ht = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ht[idKey] = value
        res = []
        while self.ptr in self.ht:
            res.append(self.ht[self.ptr])
            self.ptr += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
