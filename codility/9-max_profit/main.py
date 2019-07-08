import sys

"""
    exactly the same with lc121: Best Time to Buy and Sell Stock

    Time    O(n)
    Space   O(1)
    Reuslt  100/100
    https://app.codility.com/demo/results/trainingBE69K2-N8S/
"""


def solution(A):
    # write your code in Python 3.6
    dip = sys.maxsize
    res = 0
    for i in range(len(A)):
        a = A[i]
        dip = min(dip, a)
        res = max(res, a-dip)
    return res
