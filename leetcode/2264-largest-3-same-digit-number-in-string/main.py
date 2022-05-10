"""
    string

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def largestGoodInteger(self, s: str) -> str:
        n = len(s)
        res = ''
        res_num = 0
        for i in range(2, n):
            a = s[i-2]
            b = s[i-1]
            c = s[i]
            if a == b and b == c:
                temp = a+b+c
                x = int(temp)
                if x >= res_num:
                    res_num = x
                    res = temp
        return res
