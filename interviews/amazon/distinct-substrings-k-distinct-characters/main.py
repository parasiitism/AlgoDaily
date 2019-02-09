"""
    Find all distinct substrings with exactly k distinct characters. 
    e.g.
        s = 'abcdabc', k = 3
        return ['abc', 'bcd', 'cda', 'dab']
    
    Variation: Find all the substrings(not necessarily distinct) with exactly k distinct characters
"""


class Solution(object):
    def distinctSubstrings(self, s, k):
        """
            1st approach: brute force
            1. find all the substrings and check if each of them has only k distinct charactors using a hashtable
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


print(Solution().distinctSubstrings('abc', 2))
print(Solution().distinctSubstrings('aba', 2))
print(Solution().distinctSubstrings('aa', 1))
print(Solution().distinctSubstrings('abcdabc', 3))


class Solution(object):
    def distinctSubstrings(self, s, k):
        """
            2nd approach: better brute force

            https://www.geeksforgeeks.org/count-number-of-substrings-with-exactly-k-distinct-characters/

            1. find all the substrings and check if each of them has only k distinct charactors using a hashtable
            2. use a set to avoid duplicate substrings

            Time    O(n^2)
            Space   O(n)
        """
        res = set()
        for i in range(len(s)):
            distinct_count = 0
            m = {}
            for j in range(i, len(s)):
                c = s[j]
                if c not in m:
                    m[c] = 1
                    distinct_count += 1
                else:
                    m[c] += 1
                if distinct_count == k:  # i am not sure if dict.keys() is O(n)
                    res.add(s[i: j+1])

        return res, len(res)


print(Solution().distinctSubstrings('abc', 2))
print(Solution().distinctSubstrings('aba', 2))
print(Solution().distinctSubstrings('aa', 1))
print(Solution().distinctSubstrings('abcdabc', 3))
print(Solution().distinctSubstrings('abcbaa', 3))
