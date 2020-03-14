"""
    1st: just do what it said

    Time    O(N -> N^2)
    Space   O(N)
    140 ms, faster than 16.04%
"""


class Solution:
    def sortString(self, s: str) -> str:
        res = ''
        while len(s) > 0:
            a, b = self.f1(s)
            res += a
            s = b
            a, b = self.f2(s)
            res += a
            s = b
        return res

    def f1(self, s):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        ht = 26 * [0]
        for c in s:
            ht[ord(c)-ord('a')] += 1
        selected = ''
        for i in range(26):
            if ht[i] > 0:
                selected += alphabets[i]
                ht[i] -= 1
        remained = ''
        for i in range(26):
            if ht[i] > 0:
                remained += ht[i] * alphabets[i]
        return selected, remained

    def f2(self, s):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        ht = 26 * [0]
        for c in s:
            ht[ord(c)-ord('a')] += 1
        selected = ''
        for i in range(25, -1, -1):
            if ht[i] > 0:
                selected += alphabets[i]
                ht[i] -= 1
        remained = ''
        for i in range(26):
            if ht[i] > 0:
                remained += ht[i] * alphabets[i]
        return selected, remained
