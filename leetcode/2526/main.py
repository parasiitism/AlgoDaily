"""
    sliding window + hashtable

    Time of consec()    O(1)
    Space               O(k)
"""


class DataStream:

    def __init__(self, value: int, k: int):
        self.value, self.k = value, k
        self.ctr = Counter()
        self.arr = []

    def consec(self, num: int) -> bool:
        if len(self.arr) >= self.k:
            left = self.arr.pop(0)
            self.ctr[left] -= 1
        self.arr.append(num)
        self.ctr[num] += 1
        return self.ctr[self.value] == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
