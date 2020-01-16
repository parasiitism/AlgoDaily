from collections import defaultdict

"""
    1st: dynamic programming
    - recursion + hastable
    - iterate from the the longest string back to shortest
        - slicing every character to see if there is match in words,
        if yes recursively chopping that until we reach to the shortest word in a chain
        - for each string that we went through, record the length of the longest string chain in a hashtable to avoid redundant calculation

    Time    O(NM)
    Space   O(N)
    168 ms, faster than 42.99%
"""


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.wordSet = set(words)
        words = sorted(words, key=len, reverse=True)
        self.ht = defaultdict(int)
        self.res = 0
        for w in words:
            count = self.dfs(w)
            self.res = max(self.res, count)
        return self.res

    def dfs(self, s: str) -> bool:
        maxCount = 0
        for i in range(len(s)):
            key = s[:i] + s[i+1:]
            if key in self.wordSet:
                if key in self.ht:
                    maxCount = max(maxCount, self.ht[key])
                else:
                    count = self.dfs(key)
                    maxCount = max(maxCount, count)
        self.ht[s] = maxCount + 1
        return self.ht[s]
