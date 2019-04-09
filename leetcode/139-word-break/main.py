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

        32 ms, faster than 57.40%
        """
        wordSet = set()
        for w in wordDict:
            wordSet.add(w)
        m = {}
        return self.find(s, wordSet, m)

    def find(self, s, wordSet, m):
        if len(s) == 0:
            return True
        if s in m:
            return m[s]
        ifAnyTrue = False
        for i in range(1, len(s)+1):
            w = s[:i]
            if w in wordSet:
                temp = self.find(s[i:], wordSet, m)
                ifAnyTrue = ifAnyTrue or temp
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

print("----------------------------------------")


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        2nd approach: recursion + memorization + slice max length
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
        36 ms, faster than 37.97%
        """
        wordSet = set()
        for w in wordDict:
            wordSet.add(w)
        m = {}
        return self.find(s, wordSet, m)

    def find(self, s, wordSet, m):
        if len(s) == 0:
            return True
        if s in m:
            return m[s]
        ifAnyTrue = False

        for word in wordSet:
            w = s[:len(word)]
            if word == w:
                temp = self.find(s[len(word):], wordSet, m)
                ifAnyTrue = ifAnyTrue or temp
        # memorize the result for s,
        # then we can use it to avoid redundant computation if we meet s again
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
