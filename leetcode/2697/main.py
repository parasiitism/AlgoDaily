"""
    2 pointers
    - keep replacing the smallest characters until 2 pointers meet in the middle of the string

    Time    O(N)
    Space   O(N) the str array
"""


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        A = [c for c in s]
        while i < j:
            if A[i] == A[j]:
                i += 1
                j -= 1
            else:
                a = A[i]
                b = A[j]
                A[i] = min(a, b)
                A[j] = min(a, b)
        return ''.join(A)
