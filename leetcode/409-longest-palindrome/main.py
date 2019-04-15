"""
    1st approach: hashtable
    1. count the occurence of each character
    2. make sure the all characters occurr "evenly" by declementing the odd ocurrence characters
    3. if no of odd ocurrence characters > 0, 
        wit means that we have to place any one of them in the center to form the biggest palindrome

    Time    O(n)
    Space   O(n)
    36 ms, faster than 15.64%
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        # count the occurence of each character
        ht = {}
        for c in s:
            if c in ht:
                ht[c] += 1
            else:
                ht[c] = 1

        # make sure the all characters occurr "evenly"
        noOfOdd = 0
        res = len(s)
        for key in ht:
            if ht[key] % 2 != 0:
                res -= 1
                noOfOdd += 1

        # if no of odd ocurrence characters > 0, it means that we have to place any one of them in the center to form the biggest palindrome
        if noOfOdd > 0:
            res += 1
        return res


a = "abccccdd"
print(Solution().longestPalindrome(a))

a = "aaaabbbccccddd"
print(Solution().longestPalindrome(a))
