"""
    1st: sliding window
    - concat to make the input handle the rotation
    - make two different string with the same length by 01 and 10 alternative. 
        e.g. s = 11100
        ss  = 1110011100
        s01 = 0101010101
        s10 = 1010101010
    - compare the strings with a sliding window of length n(the original string)

    Time    O(N)
    Space   O(N)
    1087 ms, faster than 51.62%
"""


class Solution:
    def minFlips(self, s: str) -> int:
        ss = s + s
        n = len(s)
        nn = len(ss)
        s01 = ''
        s10 = ''
        for i in range(nn):
            if i % 2 == 0:
                s01 += '0'
                s10 += '1'
            else:
                s01 += '1'
                s10 += '0'
        res = 2**32
        res01 = 0
        res10 = 0
        for i in range(nn):
            if ss[i] != s01[i]:
                res01 += 1
            if ss[i] != s10[i]:
                res10 += 1
            if i >= n:
                if ss[i-n] != s01[i-n]:
                    res01 -= 1
                if ss[i-n] != s10[i-n]:
                    res10 -= 1
            if i >= n-1:
                res = min(res, res01, res10)
        return res
