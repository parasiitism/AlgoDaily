"""
    1st approach: array slicing

    Time    O(1)
    Space   O(1)
    Result 100/100 https://app.codility.com/demo/results/trainingEEW2Z6-4QB/
"""


def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0 or K <= 0:
        return A
    n = len(A)
    K = K % n
    return A[n-K:] + A[:n-K]
