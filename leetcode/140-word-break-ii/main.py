"""
    questions to ask:
    - will the words in wordDict contain each other? e.g. wordDict = [abc, ab] ? yes
    - will there be no duplicate words in wordDict? yes
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]

        My initial attempt got TLE, this is the my initial attempt+memorization
        - the trickty point is

        ref:
        - https://leetcode.com/problems/word-break-ii/discuss/44167/My-concise-JAVA-solution-based-on-memorized-DFS

        Time    O(n^3)
        Space   O(n^3)
        44 ms, faster than 47.57%
        """
        wordSet = set()
        for w in wordDict:
            wordSet.add(w)
        m = {}
        return self.find(s, wordSet, m)

    def find(self, s, wordSet, m):
        if s in m:
            return m[s]
        res = []
        if len(s) == 0:
            return [""]
        for word in wordSet:
            w = s[:len(word)]
            if w == word:
                tempList = self.find(s[len(word):], wordSet, m)
                for temp in tempList:
                    if len(temp) > 0:
                        res.append(w + " " + temp)
                    else:
                        res.append(w)
        # memorize the result for s, then we can use it to avoid redundant computation if we meet s again
        m[s] = res
        return res


s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))
print("---")

s = "catsanddog"
d = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, d))
print("---")

s = "pineapplepenapple"
d = ["apple", "pen", "applepen", "pine", "pineapple"]
print(Solution().wordBreak(s, d))
print("---")

s = "pineapplepenapple"
d = ["apple", "pen", "applepen", "pine", "pineapple", "penapple"]
print(Solution().wordBreak(s, d))
print("---")

s = "catsandog"
d = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, d))
print("---")

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
d = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa",
     "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
print(Solution().wordBreak(s, d))
