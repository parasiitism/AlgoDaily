"""
    1st approach: recursion
    - when we do recursion to slice candidates, we can check there are any palindromes from start to i, s[:i+1]
    - if yes, we can do the next recusion starting from i+1

    e.g. abcdcbe

    when it comes to the first b, the palindromes from the b are
    b
    bcdcb

    when it comes to the c, the palindromes from the c are
    c
    cdc


    ref:
    - https://leetcode.com/problems/palindrome-partitioning/discuss/42100/Python-easy-to-understand-backtracking-solution.

    Time    O(n * 2^n) the worst case all characters are the same, so for each character we can split or contain
    Space   O(n) the depth of the recursion tree
    76 ms, faster than 83.58%
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.dfs(s, [])
        return self.res

    def dfs(self, cands, path):
        if len(cands) == 0:
            self.res.append(path)
        for i in range(1, len(cands)+1):
            if self.isPalindromic(cands[:i]) == True:
                self.dfs(cands[i:], path + [cands[:i]])

    def isPalindromic(self, s):
        return s == s[::-1]
