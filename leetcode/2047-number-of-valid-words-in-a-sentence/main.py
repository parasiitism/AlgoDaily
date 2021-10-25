"""
    1st: straightforward but lengthy string checking

    Time    O(N)
    Space   O(N)
    44 ms, faster than 87.50%
"""


class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        res = 0
        for w in words:
            hyphens = []
            punctuations = []
            digits = []
            for i in range(len(w)):
                c = w[i]
                if c == '-':
                    hyphens.append((c, i))
                elif c in '!.,':
                    punctuations.append((c, i))
                elif c.isdigit():
                    digits.append((c, i))
            if len(digits) > 0:
                continue
            if len(hyphens) > 1 or len(punctuations) > 1:
                continue
            if len(hyphens) > 0:
                if hyphens[0][1] == 0 or hyphens[0][1] == len(w)-1:
                    continue
                j = hyphens[0][1]
                if w[j-1].isalpha() == False or w[j+1].isalpha() == False:
                    continue
            if len(punctuations) > 0 and (punctuations[0][1] != len(w)-1):
                continue
            res += 1
        return res
