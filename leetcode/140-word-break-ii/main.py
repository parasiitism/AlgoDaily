"""
    questions to ask:
    - will the words in wordDict contain each other? e.g. wordDict = [abc, ab] ? yes
    - will there be no duplicate words in wordDict? yes
    - lowercase letters only? yes
    - do we need to deal with punctuation? no
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]

        1st approach: top-down dfs
        - generate all possibilites by appending a valid "word" to its prefix
        - since we cant do memorization if we construct the result by top-down
        - it got TLE

        Time    O(n^n)
        Space   O(n^n)
        TLE
        """
        wordSet = set()
        for w in wordDict:
            wordSet.add(w)
        ans = self.find(s, wordSet, "")
        return ans

    def find(self, s, wordSet, path):
        res = []
        if len(s) == 0:
            return [path[1:]]
        for word in wordSet:
            w = s[:len(word)]
            if w == word:
                tempList = self.find(s[len(word):], wordSet, path+" "+w)
                res += tempList
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
print("----------------------------------------------------------------")


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]

        2nd approach is to modify the top-down approach to a bottum-up approach
        - when we reach to an empty string, it means the path it went through is one of the result

        Time    O(n^2*k)
        Space   O(n^2*k)
        TLE
        """
        wordSet = set()
        for w in wordDict:
            wordSet.add(w)
        m = {}
        ans = self.find(s, wordSet, m)
        return ans

    def find(self, s, wordSet, m):
        if len(s) == 0:
            """
            when len(s) == 0, it reaches to a result
            but since the function also returns [] if it doesn't find any result
            we want the function return something such that the parent recursive function can distinguish which recursive calls reach to a result
            e.g.1
                'apple', return [''] so that its parent can append 'apple' and return
            e.g.2
                'appl', return [] so that its parent knows there is no match in dict and wont appnd anything at the end

            see ./idea.png
            """
            return [""]
        res = []
        for word in wordSet:
            w = s[:len(word)]
            if w == word:
                tempList = self.find(s[len(word):], wordSet, m)
                for temp in tempList:
                    if len(temp) > 0:
                        res.append(w + " " + temp)
                    else:
                        res.append(w)
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
print("----------------------------------------------------------------")

"""
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]

    3rd approach: optimize the 2nd approach with memorization

    ref:
    - https://leetcode.com/problems/word-break-ii/discuss/44167/My-concise-JAVA-solution-based-on-memorized-DFS

    Time    O(n^2*k)
    Space   O(n^2*k)
    44 ms, faster than 47.57%
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        wordSet = set()
        for w in wordDict:
            wordSet.add(w)
        m = {}
        return self.find(s, wordSet, m)

    def find(self, s, wordSet, m):
        if s in m:
            return m[s]  # <- the only diff compared to 2nd approach
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
        # memorize the result for s,
        # then we can use it to avoid redundant computation if we meet s again
        m[s] = res  # <- the only diff compared to 2nd approach
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
print("----------------------------------------------------------------")
