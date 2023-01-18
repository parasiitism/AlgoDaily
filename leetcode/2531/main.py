"""
    hashtable + bruteforce

    Time    O(A+B+26*26)
    Space   O(A+B)
"""


class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        ctr1 = Counter(word1)
        ctr2 = Counter(word2)
        for c1 in 'abcdefghijklmnopqrstuvwxyz':
            for c2 in 'abcdefghijklmnopqrstuvwxyz':
                if ctr1[c1] > 0 and ctr2[c2] > 0:
                    ctr1[c1] -= 1
                    ctr2[c1] += 1
                    ctr1[c2] += 1
                    ctr2[c2] -= 1
                    if self.count_keys(ctr1) == self.count_keys(ctr2):
                        return True
                    # backtrack
                    ctr1[c1] += 1
                    ctr2[c1] -= 1
                    ctr1[c2] -= 1
                    ctr2[c2] += 1
        return False

    def count_keys(self, ctr):
        keys = 0
        for k in ctr:
            if ctr[k] > 0:
                keys += 1
        return keys
