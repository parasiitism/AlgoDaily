"""
    1st approach: count
    - similar to compress string

    Time    O(n)
    Space   O(n)
    24 ms, faster than 86.57%
"""


class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        if len(S) == 0:
            return []
        res = []
        count = 1
        for i in range(1, len(S)):
            if S[i-1] == S[i]:
                count += 1
            else:
                if count >= 3:
                    res.append([i-count, i-1])
                count = 1
        if count >= 3:
            res.append([len(S)-count, len(S)-1])
        return res
