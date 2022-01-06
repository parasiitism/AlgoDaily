"""
    1st: math

    Time    O(N)
    Space   O(1)
    317 ms, faster than 60.00%
"""


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prevOnes = 0
        for i in range(len(bank)):
            cnt = self.countOnes(bank[i])
            if cnt > 0:
                res += prevOnes * cnt
                prevOnes = cnt
        return res

    def countOnes(self, A):
        res = 0
        for c in A:
            if c == '1':
                res += 1
        return res
