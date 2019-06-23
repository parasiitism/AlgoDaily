"""
    1st approach: dfs
	- recursively go through all the possibilities
	- avoid duplicate computing by using a set
    
	Time	O(2^n)
	Space	O(2^n)
	48 ms, faster than 70.01%
"""


class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        self.res = []
        self.dfs(S, "")
        return self.res

    def dfs(self, remain, s):
        if len(remain) == 0:
            self.res.append(s)
        else:
            first = remain[0]
            if (ord(first) >= 65 and ord(first) <= 90) or\
                    (ord(first) >= 97 and ord(first) <= 122):
                self.dfs(remain[1:], s+first.lower())
                self.dfs(remain[1:], s+first.upper())
            else:
                self.dfs(remain[1:], s+first)
