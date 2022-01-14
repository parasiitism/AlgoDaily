"""
    1st: hashtable
    - transfrom every startWord into a signature 26*[0], and put it into a hashset
    - for every target word, remove every character and check if the transformed signature is in the hashset
    - accumulate the founds

    Time    O(26S + 26*26T)
    Space   O(26S)
    1713 ms, faster than 50.00%
"""


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startSet = set()
        for w in startWords:
            A = self.word2Sig(w)
            key = tuple(A)
            startSet.add(key)
        res = 0
        for w in targetWords:
            A = self.word2Sig(w)
            for i in range(26):
                if A[i] == 1:
                    A[i] = 0
                    key = tuple(A)
                    A[i] = 1
                    if key in startSet:
                        res += 1
                        break
        return res

    def word2Sig(self, w):
        A = 26 * [0]
        for c in w:
            idx = ord(c) - ord('a')
            A[idx] += 1
        return A
