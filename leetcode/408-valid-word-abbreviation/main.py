"""
    1st approach: brute force
    - contruct a string from abbr
    - compare word with that string

    Time    O(n)
    Space   O(n)
    32 ms, faster than 12.99%
"""


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        s = ''
        num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and int(c) == 0:
                    return False
                num = num*10 + int(c)
            else:
                if num > 0:
                    s += num * '#'
                    num = 0
                s += c
        if num >= 999999999:
            return False
        if num > 0:
            s += num * '#'
            num = 0
        if len(s) != len(word):
            return False
        for i in range(len(word)):
            if s[i] != '#' and word[i] != s[i]:
                return False
        return True


a = 'internationalization'
b = 'i12iz4n'
print(Solution().validWordAbbreviation(a, b))

a = 'apple'
b = 'a2e'
print(Solution().validWordAbbreviation(a, b))

a = 'bignumberhahaha'
b = '999999999'
print(Solution().validWordAbbreviation(a, b))
