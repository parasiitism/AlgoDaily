"""
    1st approach: math
    check if A + B > C

    Time    O(n)
    Space   O(1)
    Result 100/100 https://app.codility.com/demo/results/trainingU9WTZY-W36/
"""


def solution(A):
    # write your code in Python 3.6
    A = sorted(A)
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0
