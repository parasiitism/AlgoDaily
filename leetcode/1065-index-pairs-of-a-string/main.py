"""
    1st approach: brute force + hashtable
    1. generate all the substrings
    2. check if each substring is one of the words

    Time    O(W + T^T)
    Space   O(W)
    64 ms, faster than 6.67%
"""


class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        wordSet = set(words)
        for i in range(len(text)):
            for j in range(i, len(text)):
                sub = text[i:j+1]
                if sub in wordSet:
                    res.append([i, j])
        return res


a = "thestoryofleetcodeandme"
b = ["story", "fleet", "leetcode"]
print(Solution().indexPairs(a, b))

a = "ababa"
b = ["aba", "ab"]
print(Solution().indexPairs(a, b))

a = "ababa"
b = ["ab", "aba"]
print(Solution().indexPairs(a, b))

print("-----")

"""
    1st approach: substring
    - for each word, iterate through the text to find if there is a substring which matches the word 

    Time    O(WTk)
    Space   O(W)
    20 ms, faster than 98.10%
"""


class Solution(object):
    def indexPairs(self, text, words):
        """
        :type text: str
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        for word in words:
            for i in range(len(text)):
                sub = text[i:i+len(word)]
                if word == sub:
                    res.append([i, i+len(word)-1])
        return res


a = "thestoryofleetcodeandme"
b = ["story", "fleet", "leetcode"]
print(Solution().indexPairs(a, b))

a = "ababa"
b = ["aba", "ab"]
print(Solution().indexPairs(a, b))

a = "ababa"
b = ["ab", "aba"]
print(Solution().indexPairs(a, b))
