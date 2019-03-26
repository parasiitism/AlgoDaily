class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        1st approach: recursion + memorization
        - e.g. "catsandogab", ["cats", "dog", "sand", "and", "cat", "og", "ab"]
        from the begining, we can split it into 2 strings
        [cat,sandogab], [cats, andogab]
        then they can become in the next recursion
        [cat,sand,ogab], [cat,sand,ogab]
        then 
        [cat,sand,og,ab], [cat,sand,og,ab]
        - actually we did [cat,sand,ogab], we know that "ogab" is breakable after the recursion,
        therefore we can save "ogab" as "true" so that we can avoid redundant computation if we meet "ogab" again

        Time    O(n^2)
        Space   O(n)
        28 ms, faster than 74.77%
        """
        wordSet = set()
        maxLength = 0
        for w in wordDict:
            maxLength = max(maxLength, len(w))
            wordSet.add(w)
        m = {}
        return self.find(s, wordSet, maxLength, m)

    def find(self, s, wordSet, maxLength, m):
        if len(s) == 0:
            return True
        if s in m:
            return m[s]
        ifAnyTrue = False
        for i in range(1, maxLength+1):
            if i <= len(s):
                w = s[:i]
                if w in wordSet:
                    temp = self.find(s[i:], wordSet, maxLength, m)
                    ifAnyTrue = ifAnyTrue or temp
        # memorize the result for s, then we can use it to avoid redundant computation if we meet s again
        m[s] = ifAnyTrue
        return ifAnyTrue


s = "applepenapple"
d = ["apple", "pen"]
print(Solution().wordBreak(s, d))

s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))

s = "catsanddog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))

s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat", "og"]
print(Solution().wordBreak(s, d))

a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
d = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
     "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(Solution().wordBreak(s, d))
