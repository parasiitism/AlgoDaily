"""
    1st: brute force

    Time    O(NM)
    Space   O(1)
    68 ms, faster than 35.95%
"""


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        i = 0
        while True:
            if tickets[i] > 0:
                tickets[i] -= 1
                res += 1
            if tickets[i] == 0 and i == k:
                return res
            i += 1
            if i == len(tickets):
                i = 0
        return -1
