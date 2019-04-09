class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int

        1st approach: 2pointers
        - same idea as lc143

        Time    O(n)
        Space   O(n)
        48 ms, faster than 21.34%
        """
        if word1 == word2:
            last = -1
            res = len(words)
            for i in range(len(words)):
                if words[i] == word1:
                    if last != -1:
                        res = min(res, i-last)
                    last = i
            return res
        p1 = -1
        p2 = -1
        res = len(words)
        for i in range(len(words)):
            word = words[i]
            if word == word1:
                p1 = i
            if word == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                res = min(res, abs(p1-p2))
        return res
