"""
    hashtable

    Time    O(26N)
    Space   O(26)
    54 ms, faster than 100.00%
"""


class Solution:
    def equalFrequency(self, word: str) -> bool:
        ctr = Counter(word)
        for key in ctr:
            ctr[key] -= 1
            if self.checkIfAllEqual(ctr):
                return True
            ctr[key] += 1
        return False

    def checkIfAllEqual(self, ht):
        counts = set()
        for key in ht:
            c = ht[key]
            if c > 0:
                counts.add(c)
        return len(counts) == 1
