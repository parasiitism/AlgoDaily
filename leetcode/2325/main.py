"""
    Hashtable

    Time    O(N)
    Space   O(N)
    53 ms, faster than 57.94%
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = {}
        i = 0
        for c in key:
            if c != ' ' and c not in mapping:
                mapping[c] = i
                i += 1
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        res = ""
        for c in message:
            if c in mapping:
                i = mapping[c]
                res += alphabets[i]
            else:
                res += " "
        return res
