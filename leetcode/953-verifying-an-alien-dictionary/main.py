"""
    1st: brute force with a hashtable

    Time    O(MN)
    Space   O(N)
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        orderMap = {}
        for i in range(len(order)):
            orderMap[order[i]] = i
        for i in range(1, len(words)):
            prev = words[i-1]
            curr = words[i]
            minLen = min(len(prev), len(curr))
            shouldNext = False
            for j in range(minLen):
                a = orderMap[prev[j]]
                b = orderMap[curr[j]]
                if a < b:
                    shouldNext = True
                    break
                elif a == b:
                    continue
                else:
                    return False
            if shouldNext:
                continue
            if prev[:minLen] == curr[:minLen] and len(prev) > len(curr):
                return False
        return True
