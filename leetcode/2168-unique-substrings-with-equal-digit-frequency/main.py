"""
    1st: brute force hashtable

    Time    O(N^2)
    Space   O(N^2)
    3504 ms, faster than 100.00% 
"""


class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        res = set()
        for i in range(n):
            cnter = 10 * [0]
            ss = ''
            for j in range(i, n):
                d = int(s[j])
                cnter[d] += 1
                ss += s[j]
                freqs = set(cnter)
                if 0 in freqs:
                    freqs.remove(0)
                if len(freqs) == 1:
                    res.add(ss)
        return len(res)
