"""
    1st: math
    - for every vowel, there can be (i+1) * (n-i) substrings contain it

    012345678901
    qwrtAzxcvbnm
        ^
    -----_______
     i+1   n-i
      5  *  7   = at idx4, where A is, there are total 35 substrings contain it

    Time    O(N)
    Space   O(1)
    108 ms, faster than 100.00%
"""


class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        res = 0
        for i in range(n):
            if word[i] in 'aeiou':
                res += (i+1) * (n-i)
        return res
