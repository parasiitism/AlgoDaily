"""
    Find all distinct substrings with exactly k distinct characters. 
    e.g.
        s = 'abcdabc', k = 3
        return ['abc', 'bcd', 'cda', 'dab'...]
"""


class Solution(object):
    """
    1st approach: use an index to indicate the current value, append the accumulater until the length=k
    """

    def __init__(self):
        self.result = []

    def distinctSubstrings(self, s, k):
        self.dfs(s, k, '', 0)
        return self.result

    def dfs(self, s, k, acc, cur):
        if len(acc) == k:
            self.result.append(acc)
            return
        for i in range(cur, len(s)):
            self.dfs(s, k, acc+s[i], i+1)


print(Solution().distinctSubstrings('abcd', 3))


class Solution1(object):
    """
    2nd approach: substring input recursively
    """

    def __init__(self):
        self.result = []

    def distinctSubstrings(self, s, k):
        self.dfs(s, k, '')
        return self.result

    def dfs(self, s, k, acc):
        if len(acc) == k:
            self.result.append(acc)
            return
        for i in range(len(s)):
            self.dfs(s[i+1:], k, acc+s[i])


print(Solution1().distinctSubstrings('abcd', 3))
