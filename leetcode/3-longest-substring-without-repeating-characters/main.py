"""
    2nd approach: sliding window + hashtable
	- in each iteration, if we meet a 2-occurence character
        - we move the slow pointer to the left
        - and increment the count of the character on the index where slow pointer points to
        - continue to move the slow pointer until the current character's count becomes 1

	Time	O(2n)
	Space	O(n)
    56 ms, faster than 68.14%
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = {}
        left = 0
        res = 0
        for i in range(len(s)):
            c = s[i]
            if c not in ht:
                ht[c] = 1
                res = max(res, i-left+1)
            else:
                ht[c] += 1

            while ht[c] > 1:
                last = s[left]
                ht[last] -= 1
                if ht[last] == 0:
                    del ht[last]
                left += 1
        return res


a = "abcabcbb"
print(Solution().lengthOfLongestSubstring(a))

a = "bbbbb"
print(Solution().lengthOfLongestSubstring(a))

a = "pwwkew"
print(Solution().lengthOfLongestSubstring(a))

a = "abcdef"
print(Solution().lengthOfLongestSubstring(a))

a = "abcbdef"
print(Solution().lengthOfLongestSubstring(a))

a = "abcbdee"
print(Solution().lengthOfLongestSubstring(a))

a = "abb"
print(Solution().lengthOfLongestSubstring(a))

a = "ab"
print(Solution().lengthOfLongestSubstring(a))

a = "a"
print(Solution().lengthOfLongestSubstring(a))
