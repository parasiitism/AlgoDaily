"""
    1st approach: bit XOR

    Time    O(n)
    Space   O(1)
    Result 100/100 https://app.codility.com/demo/results/trainingVSKS9H-QP5/
"""


def solution(A):
    # write your code in Python 3.6
    merged = 0
    for x in A:
        merged ^= x
    return merged
