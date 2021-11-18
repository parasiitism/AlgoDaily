"""
    1st: math

    Time    O(N)
    Space   O(N)
    776 ms, faster than 60.64%
"""


class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        R = rows
        C = len(encodedText) // R
        res = []
        for i in range(C):
            j = i
            while j < len(encodedText):
                res.append(encodedText[j])
                j += C
                j += 1
        return ''.join(res).rstrip()
