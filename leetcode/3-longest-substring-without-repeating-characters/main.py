from collections import Counter
"""
    2nd approach: sliding window + hashtable
    - similar to lc3, 159, 340, 904
	- in each iteration, if we meet a 2-occurence character
        - we move the slow pointer to the left
        - and increment the count of the character on the index where slow pointer points to
        - continue to move the slow pointer until the current character's count becomes 1

	Time	O(2n)
	Space	O(n)
    60 ms, faster than 52.92%
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        counter = Counter()
        j = 0
        for i in range(len(s)):
            c = s[i]
            counter[c] += 1
            while counter[c] > 1:
                left = s[j]
                j += 1
                counter[left] -= 1
            res = max(res, i - j + 1)
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

print("-----")

"""
    followup: print that substring

    Time	O(2n)
	Space	O(n)
    64 ms, faster than 46.35%
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ht = Counter()
        j = 0
        res_left, res_right = 0, 0
        for i in range(len(s)):
            c = s[i]
            ht[c] += 1
            while ht[c] > 1:
                left = s[j]
                ht[left] -= 1
                j += 1
            if i - j + 1 > res_right - res_left + 1:
                res_left = j
                res_right = i
        return s[res_left: res_right+1]


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
