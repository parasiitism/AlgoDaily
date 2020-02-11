from typing import List

"""
    1st:
    - create a matrix with dimension of R = max(len(each word)) , C = len(words)
    - put the words into the matrix in a vertically manner
    - right strip the result and return

    Time    O(RC)
    Space   O(RC)
    28 ms, faster than 64.80%
"""


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        target_rows = max([len(w) for w in words])
        target_cols = len(words)

        matrix = []
        for _ in range(target_rows):
            matrix.append(target_cols * [' '])

        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                matrix[j][i] = word[j]

        res = []
        for arr in matrix:
            s = ''.join(arr)
            res.append(s.rstrip())

        return res
