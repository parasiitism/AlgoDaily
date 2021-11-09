"""
    1st: brute force + clumsy logic
    Time    O(N^2)
    Space   O(1)
    64 ms, faster than 100.00% 
"""


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        vowels = 'aeiou'
        res = 0
        for i in range(n):
            if word[i] not in vowels:
                continue
            vowel_chars = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                vowel_chars.add(word[j])
                if len(vowel_chars) == 5:
                    res += 1
        return res
