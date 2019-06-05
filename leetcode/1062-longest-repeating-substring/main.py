"""
    1st approach: hashtable
	- generate all the substrings and count the occurence of each
	- the result is the substring with max length and appears more than once

	Time	O(n^2)
	Space	O(n^2)
	LTE but beats 100% in golang LOL
"""


class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        ht = {}
        for i in range(len(S)):
            for j in range(i, len(S)):
                sub = S[i:j+1]
                if sub not in ht:
                    ht[sub] = 1
                else:
                    ht[sub] += 1
        res = 0
        for key in ht:
            if ht[key] > 1:
                res = max(res, len(key))
        return res


print(Solution().longestRepeatingSubstring("abcd"))
print(Solution().longestRepeatingSubstring("abbaba"))
print(Solution().longestRepeatingSubstring("aabcaabdaab"))
print(Solution().longestRepeatingSubstring("aaaa"))
print(Solution().longestRepeatingSubstring("baaabaaabaaab"))
