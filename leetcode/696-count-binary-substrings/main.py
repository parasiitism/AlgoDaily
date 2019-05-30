"""
    1st approach: counting

    e.g. 000111100
    
    0123456789AB <- index
    ------------
    000111100111
      ^   ^ ^  ^
      3   4
            2  3
    when we reach to index7, we add min(3, 4) to the result, and reset zeroCount = 0
    when we reach to index9, we add min(2, 4) to the result, add reset oneCount = 0
    when we reach to the end, we add min(2, 3) to the reuslt
    
    Time    O(n)
    Space   O(1)
    340 ms, faster than 12.29%
"""


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        zeroCount = 0
        oneCount = 0
        res = 0
        for i in range(len(s)):
            if i > 0 and s[i-1] != s[i]:
                res += min(zeroCount, oneCount)
                if s[i] == '0':
                    zeroCount = 0
                else:
                    oneCount = 0
            if s[i] == '0':
                zeroCount += 1
            if s[i] == '1':
                oneCount += 1
        res += min(zeroCount, oneCount)
        return res
