"""
    1st: hashtable

    Time    O(N)
    Space   O(N)
    36 ms, faster than 57.14%
"""


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        count1 = 26 * [0]
        count2 = 26 * [0]
        for i in range(len(word1)):
            c1 = word1[i]
            count1[ord(c1)-ord('a')] += 1
            c2 = word2[i]
            count2[ord(c2)-ord('a')] += 1
        for i in range(26):
            if abs(count1[i] - count2[i]) > 3:
                return False
        return True
