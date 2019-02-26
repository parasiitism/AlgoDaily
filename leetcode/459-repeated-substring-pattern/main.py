class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        1st approach: replace string
        - for each sub, check if the remaining string will be empty if we replace the substring with empty

        Time    O(n^2)
        Space   O(1)
        3604 ms, faster than 5.09%
        """
        for i in range(1, len(s)/2+1):
            sub = s[:i]
            if self.check(s[i:], sub) == True:
                return True
        return False

    def check(self, s, sub):
        x = s.replace(sub, "")
        return len(x) == 0


print(Solution().repeatedSubstringPattern("a"))
print(Solution().repeatedSubstringPattern("ab"))
print(Solution().repeatedSubstringPattern("aa"))
print(Solution().repeatedSubstringPattern("aaa"))
print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("ababa"))
print(Solution().repeatedSubstringPattern("abcabc"))
print(Solution().repeatedSubstringPattern("abccda"))
