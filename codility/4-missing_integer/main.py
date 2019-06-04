"""
    similar to lc41:

    Time    O(n)
    Space   O(n)
    Result 100/100 https://app.codility.com/demo/results/trainingRGB6YN-6KE/
"""


def solution(A):
    # write your code in Python 3.6
    hs = set()
    for a in A:
        hs.add(a)
    for i in range(1, len(A) + 1):
        if i not in hs:
            return i
    return len(A) + 1
