"""
    1st approach: hashset
    1. put the words into a set
    2. for each word, i check if the word can be built up from the words
    3. update the result if necessary

    Time    O(nk) n: number of words, k: average number of characters in words
    Space   O(n)
    120 ms, faster than 38.44%
"""


class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        res = ""
        wordSet = set(words)
        for word in words:
            canBuild = True
            for i in range(1, len(word)+1):
                subs = word[:i]
                if subs not in wordSet:
                    canBuild = False
                    break
            if canBuild == True:
                if res == "":
                    res = subs
                elif len(subs) > len(res):
                    res = subs
                elif len(subs) == len(res) and subs < res:
                    res = subs
        return res


a = ["w", "wo", "wor", "worl", "world"]
print(Solution().longestWord(a))

a = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution().longestWord(a))

a = ["a"]
print(Solution().longestWord(a))

a = []
print(Solution().longestWord(a))

a = ["m", "mo", "moc", "moch", "mocha", "l", "la",
     "lat", "latt", "latte", "c", "ca", "cat"]
print(Solution().longestWord(a))
