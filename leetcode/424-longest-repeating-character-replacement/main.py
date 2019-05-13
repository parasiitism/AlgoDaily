"""
    1st approach: hashtable + 2 pointers
    - the basic idea is if we dont have k, 
        what is the minimum number of characters to replace such that we can form the result?
    - the ans is the length of the string - maxOccurence of a character
    - so if we k limit, we can do it with a window

    e.g. AAAABCD

    AAAABCD
    ^   ^
    when i == 4, the AAAAB is valid cos we can remove B to form AAAAA

    AAAABCD
    ^    ^
    when i == 5, the AAAAB is not valid so we should remove one character from the left, so it becomes

    AAAABCD
     ^   ^
    BUT be careful, we dont need to remove further because we just need to max length. 
    if the window contains ABCDE but the count is still 5, the result is still 5 which was made by AAAAB

    learned from others
    - https://www.cnblogs.com/grandyang/p/5999050.html

    Time    O(n)
    Space   O(n)
    96 ms, faster than 82.46%
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        seen = 26*[0]
        maxCnt = 0
        res = 0
        left = 0
        for i in range(len(s)):
            idx = ord(s[i]) - ord('A')
            seen[idx] += 1
            maxCnt = max(maxCnt, seen[idx])
            if i-left+1-maxCnt > k:
                key = ord(s[left]) - ord('A')
                seen[key] -= 1
                left += 1
            res = max(res, i-left+1)
        return res


"""
    followup: find the substring
    - if there are more than one, give me the first one

    Time    O(nk)
    Space   O(n)
    148 ms, faster than 46.92%
"""


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        seen = 26*[0]
        res = ""
        left = 0
        for i in range(len(s)):
            idx = ord(s[i]) - ord('A')
            seen[idx] += 1
            if i-left+1-max(seen) > k:
                key = ord(s[left]) - ord('A')
                seen[key] -= 1
                left += 1
            if i-left+1 > len(res):
                res = s[left:i+1]
        return res


print(Solution().characterReplacement("ABAB", 2))
print(Solution().characterReplacement("AABABBA", 1))
print(Solution().characterReplacement("AAAABCD", 2))
print(Solution().characterReplacement("AAAABCDAAAA", 3))
