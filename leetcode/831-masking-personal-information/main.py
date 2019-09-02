"""
    1st: simple but tedious checking

    Time    O(n)
    Space   O(n)
    20 ms, faster than 31.16%
"""


class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            S = S.lower()
            temp = S.split('@')
            name, addr = temp[0], temp[1]
            res = name[0] + '*****' + name[-1] + '@' + addr
            return res
        s = ''
        for c in S[::-1]:
            if c.isdigit():
                s += c
        cnt = 0
        res = ''
        for i in range(len(s)):
            c = s[i]
            cnt += 1
            if cnt < 5:
                res += c
            else:
                res += "*"
            if cnt == 4 or cnt == 7 or (cnt == 10 and i+1 < len(s)):
                res += '-'
        if cnt > 10:
            res += '+'

        return res[::-1]
