"""
    1st approach: hashset + string manipulation

    Time    O(n) n: number of words in sentence
    Space   O(S) the result
    12 ms, faster than 99.03%
"""


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        res = []
        words = S.split()
        for i in range(len(words)):
            word = words[i]
            if word[0] not in vowels:
                word = word[1:] + word[0]
            res.append(word + 'ma' + (i+1)*'a')
        return " ".join(res)
