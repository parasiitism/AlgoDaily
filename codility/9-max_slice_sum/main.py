import sys

"""
    exactly the same with lc53: Maximum Subarray

    Time    O(n)
    Space   O(1)
    Reuslt  100/100
    https://app.codility.com/demo/results/trainingJE7K9Q-THU/
"""


def solution(A):
    # write your code in Python 3.6
    cur = -sys.maxsize
    res = -sys.maxsize
    for i in range(len(A)):
        cur = max(cur+A[i], A[i])
        res = max(res, cur)
    return res
