"""
    1st:
    - transform to string and replace 6 with 9
    - transform back to number and compare with the temporary result

    Timr    O(NM)
    Space   O(N)
    28 ms, faster than 57.76%
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        res = num
        s = str(num)
        for i in range(len(s)):
            c = s[i]
            if c == '6':
                n = int(s[:i] + '9' + s[i+1:])
                res = max(res, n)
        return res
