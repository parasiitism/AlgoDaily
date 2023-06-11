from collections import *

"""
    2 hashtables
    - one for the numbers
    - another one for the frequency of those numbers

    Time of add()           O(1)
    Time of deleteOne()     O(1)
"""


class FrequencyTracker:

    def __init__(self):
        self.ctr = {}
        self.ctr2 = Counter()

    def add(self, number: int) -> None:
        if number not in self.ctr:
            self.ctr[number] = 0
        orig_freq = self.ctr[number]
        self.ctr[number] += 1
        new_freq = self.ctr[number]
        self.ctr2[orig_freq] -= 1
        self.ctr2[new_freq] += 1

    def deleteOne(self, number: int) -> None:
        if number not in self.ctr:
            return
        orig_freq = self.ctr[number]
        self.ctr[number] -= 1
        new_freq = self.ctr[number]
        self.ctr2[orig_freq] -= 1
        self.ctr2[new_freq] += 1

        if self.ctr[number] == 0:
            del self.ctr[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.ctr2[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
