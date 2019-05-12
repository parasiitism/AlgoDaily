"""
    1st approach: string checking
    - check if each of the words can be formed by deleting characters from s
    - there are 2 conditions to update the intermediate result
        1. length of this word is longer than the intermediate result
        2. this word is lexicologically lower than intermediate result if both lengths are the same
    
    Time    O(nk) n: number of the words in dictionary, k: length of the s
    Space   O(k) at worst case it would be s
    224 ms, faster than 77.90%
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ''
        for word in d:
            if self.check(s, word):
                # conditions
                # 1. length of this word is longer than the intermediate result
                # 2. this word is lexicologically lower than intermediate result if both lengths are the same
                if len(word) > len(res) or len(word) == len(res) and word < res:
                    res = word
        return res

    # check if each of the words can be formed by deleting characters from s
    def check(self, s, w):
        i = 0
        for c in s:
            if c == w[i]:
                i += 1
                if i == len(w):
                    return True
        return False
