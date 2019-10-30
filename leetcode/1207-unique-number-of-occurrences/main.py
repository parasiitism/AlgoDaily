from collections import defaultdict

"""
    1st: hashtbale

    Time    O(2n)
    Space   O(n)
    24 ms, faster than 62.04%
"""
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        numCounts = defaultdict(int)
        for x in arr:
            numCounts[x] += 1
        seen = set()
        for key in numCounts:
            if numCounts[key] in seen:
                return False
            seen.add(numCounts[key])
        return True