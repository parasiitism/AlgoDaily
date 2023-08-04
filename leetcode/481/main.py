"""
    1st: simulation
    - very painful to understand the question

    Time    O(N)
    Space   O(N)
"""


class Solution:
    def magicalString(self, n: int) -> int:
        A = [1, 2, 2]
        i = 2
        cur = 1
        while len(A) < n:
            f = A[i]
            A += f * [cur]  # keep adding occurence of digit(s) in the array
            i += 1
            cur = 3 - cur  # alternating between 1 and 2
        return A[:n].count(1)
