"""
    1st: hashtable

    Time    O(n)
    Space   O(n)
    28ms beats 91ms
"""


class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        ht = {}
        for i in range(len(keyboard)):
            c = keyboard[i]
            ht[c] = i
        res = 0
        prev = 0
        for c in word:
            res += abs(ht[c]-prev)
            prev = ht[c]
        return res
