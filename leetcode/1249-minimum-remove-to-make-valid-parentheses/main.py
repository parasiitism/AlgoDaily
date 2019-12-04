"""
    1st: stack + hashtable
    - similar to lc921 but save the indices of the redundant opens & closes
    - construct the result by removing the characters at redundant indices
    
    Time    O(2N)
    Space   O(N)
    1628 ms, faster than 22.84%
"""


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        opens, closes = [], []
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                opens.append(i)
            elif c == ')':
                if len(opens) == 0:
                    closes.append(i)
                else:
                    opens.pop()
        hs = set(opens+closes)
        res = ''
        for i in range(len(s)):
            if i not in hs:
                res += s[i]
        return res
