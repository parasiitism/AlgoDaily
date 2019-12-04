"""
    1st: stack + hashtable
    - similar to lc921 but save the indices of the redundant opens & closes
    - construct the result by removing the characters at redundant indices
    
    Time    O(2N)
    Space   O(N)
    1628 ms, faster than 22.84%
"""


class Solution(object):
    def minRemoveToMakeValid(self, S):
        """
        :type s: str
        :rtype: str
        """
        if len(S) == 0:
            return 0
        opens = []
        closes = []
        for i in range(len(S)):
            c = S[i]
            if c == '(':
                opens.append(i)
            elif c == ')':
                if len(opens) == 0:
                    closes.append(i)
                else:
                    opens.pop()
        hs = set()
        for x in opens:
            hs.add(x)
        for x in closes:
            hs.add(x)
        res = ''
        for i in range(len(S)):
            if i not in hs:
                res += S[i]
        return res
