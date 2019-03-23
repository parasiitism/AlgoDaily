class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int

        1st approach: use a var for previous symbol

        Time    O(n)
        Space   O(1)
        68 ms, faster than 99.19%
        """
        indeces = {
            "I": 0,
            "V": 1,
            "X": 2,
            "L": 3,
            "C": 4,
            "D": 5,
            "M": 6,
        }

        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0
        prev = None

        for c in s:
            if prev == None:
                prev = c
            elif indeces[c] <= indeces[prev]:
                res += m[prev]
                prev = c
            else:
                val = m[c] - m[prev]
                res += val
                prev = None

        if prev != None:
            res += m[prev]

        return res
