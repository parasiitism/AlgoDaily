"""
    1st approach: brute force

    Time    O(nnk)
    Space   O(n)
    LTE
"""


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        cands = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                can = words[i] + words[j]
                if self.isPalindrome(can):
                    cands.append([i, j])
        return cands

    def isPalindrome(self, s):
        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True
        return s == s[::-1]


a = ["abcd", "dcba", "lls", "s", "sssll"]
print(Solution().palindromePairs(a))

a = ["bat", "tab", "cat"]
print(Solution().palindromePairs(a))

print("--------------------")

"""
    2nd approach: learned from others

    idea:
    - for each prefix, if it is a palindrome, check if the reversed corresponding suffix is in the input array
    - same thing for each suffix
    
    e.g. [sssll, s, lls]
    
    for sssll, prefixes are
    ''    -> sssll -> llsss
    s     -> ssll  -> llss
    ss    -> sll   -> lls
    sss   -> ll    -> ll
    sssl  -> not palindrome wont process
    sssll -> not palindrome wont process

    for sssll, prefixes are
    l     -> sssl  -> lsss
    ll    -> sss   -> sss
    sll   -> not palindrome wont process
    ssll  -> not palindrome wont process
    sssll -> not palindrome wont process

    ref:
    https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation


    Time    O(n*k^2) n: number of words, k: average length of every word
    Space   O(2n!) for every word at worse,  we save all prefixes and suffixes
    676 ms, faster than 48.46%
"""


class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        ht = {}
        for i in range(len(words)):
            ht[words[i]] = i

        res = []
        for idx in range(len(words)):
            word = words[idx]
            n = len(word)
            for i in range(n+1):
                prefix = word[:i]
                suffix = word[i:]
                if self.isPalindrome(prefix):
                    rStr = self.reverseStr(suffix)
                    if rStr != word and rStr in ht:
                        res.append([ht[rStr], idx])
                if i != n and self.isPalindrome(suffix):
                    rStr = self.reverseStr(prefix)
                    if rStr != word and rStr in ht:
                        res.append([idx, ht[rStr]])
        return res

    def isPalindrome(self, s):
        return s == s[::-1]

    def reverseStr(self, s):
        return s[::-1]


a = ["abcd", "dcba", "lls", "s", "sssll"]
print(Solution().palindromePairs(a))

a = ["bat", "tab", "cat"]
print(Solution().palindromePairs(a))
