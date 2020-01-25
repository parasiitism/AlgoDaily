"""
    1st: array
    - iterate the string in a reverse order
    - if we see a #, take the next 2 chars and map back to an alphabet
    - else, just map back to an alphbet

    Time    O(N)
    Space   O(N)
    28 ms, faster than 72.26%
"""


class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                num = s[i-2:i]
                res = self.int2char(num) + res
                i -= 3
            else:
                res = self.int2char(s[i]) + res
                i -= 1
        return res

    def int2char(self, s: str) -> str:
        n = int(s)
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        return alphabets[n-1]
