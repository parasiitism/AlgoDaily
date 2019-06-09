"""
    1st approach: sort
    - sort the array
    - the biggest number is either A[0] * A[1] * A[-1] or A[-3] * A[-2] * A[-1]

    Time    O(nlogn)
    Space   O(1)
    Result 100/100 https://app.codility.com/demo/results/trainingDWDFFD-ZDR/
"""


def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    a = A[0] * A[1] * A[-1]
    b = A[-3] * A[-2] * A[-1]
    return max(a, b)
