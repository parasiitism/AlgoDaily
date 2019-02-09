"""
    Find all distinct substrings with exactly k distinct characters. 
    e.g.
        s = 'abcdabc', k = 3
        return ['abc', 'bcd', 'cda', 'dab']
"""


class Solution(object):
    def distinctSubstrings(self, s, k):
        """
            1st approach: brute force
            1. find all the substrings and check if each of them has only k distinct charactors
            2. use a set to avoid duplicate substrings

            Time    O(n^3)
            Space   O(n)
        """
        res = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                t = s[i:j+1]
                if self.check(t, k):
                    res.add(t)
        return res, len(res)

    def check(self, s, k):
        m = {}
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1
        if len(m.keys()) == k:
            return True
        return False


print(Solution().distinctSubstrings('abcdabc', 3))
