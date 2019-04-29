"""
    1st approach: use a var for previous symbol

    Time    O(n)
    Space   O(1)
    68 ms, faster than 99.19%
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
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


"""
    2nd approach:
    - compare with prev value and if prev value < cur value
        1. undo previous addition
        2. add m[cur] - m[prev]
    - if no smaller bigger values, just do addition

    Time    O(n)
    Space   O(1)
    52 ms, faster than 97.49%
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        m = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = m[s[0]]
        for i in range(1, len(s)):
            prev = s[i-1]
            cur = s[i]
            if m[prev] < m[cur]:
                res -= m[prev]
                res += m[cur] - m[prev]
            else:
                res += m[cur]
        return res
