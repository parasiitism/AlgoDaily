"""
    1st approach: hashtable

    Time    O(n)
    Space   O(n)
    16 ms, faster than 99.31%
"""


class Solution(object):
    def wordPattern(self, pattern, sentence):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = sentence.split()
        if len(pattern) != len(words):
            return False
        forward = {}
        backward = {}
        for i in range(len(pattern)):
            c = pattern[i]
            word = words[i]
            if c not in forward:
                forward[c] = word
            elif forward[c] != word:
                return False
            if word not in backward:
                backward[word] = c
            elif backward[word] != c:
                return False
        return True


"""
    2nd approach: hashtable but calculate signature

    - Compute a word's "signature"
    
    e.g.1
    bbacyba
    0012301

    e.g.2
    xxyzwxy
    0012301

    Time    O(n)
    Space   O(n)
    16 ms, faster than 99.31%
"""


class Solution(object):
    def wordPattern(self, pattern, sentence):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = sentence.split()
        if len(pattern) != len(words):
            return False
        s1 = self.calSignature(pattern)
        s2 = self.calSignature(words)
        return s1 == s2

    def calSignature(self, s):
        signature = ""
        seen = {}
        nth = 0
        for c in s:
            if c not in seen:
                seen[c] = str(nth)
                nth += 1
            signature += seen[c] + '#'
        return signature
