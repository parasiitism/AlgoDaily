"""
    questions to ask:
    - will there be duplicates in the words? yes
    - will there be empty string in words? no. yes for followup
    - will the S be empty? no. yes for followup
"""

"""
    1st approach: brute force
    - iterate the words and check if subsequnce using the way like lc392

    Time    O(NK)
    Space   O(1)
    2004 ms, faster than 7.80%
"""


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        m = {}
        for word in words:
            if word not in m:
                m[word] = 1
            else:
                m[word] += 1

        count = 0
        for key in m:
            if self.isSubsequence(S, key) == True:
                count += m[key]
        return count

    def isSubsequence(self, S, word):
        if len(word) == 0:
            return True
        i = 0
        for c in S:
            if c == word[i]:
                i += 1
            if i == len(word):
                return True
        return False
