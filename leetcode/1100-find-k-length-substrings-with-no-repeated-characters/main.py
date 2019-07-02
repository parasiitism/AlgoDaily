"""
    1st approach: sliding window + hashtable
    - similar to lc195,395

    Time    O(26S)
    Space   O(26)
    104 ms, faster than 13.70%
"""


class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        res = 0
        counts = 26 * [0]
        for i in range(len(S)):
            if i >= K:
                last = S[i-K]
                idx = ord(last) - ord('a')
                counts[idx] -= 1
            c = S[i]
            idx = ord(c) - ord('a')
            counts[idx] += 1
            if self.ifAllOnes(counts, K):
                res += 1
        return res

    def ifAllOnes(self, counts, K):
        cnt = 0
        for i in range(len(counts)):
            if counts[i] > 1:
                return False
            cnt += counts[i]
        return cnt == K
