"""
    1st approach: math

    Time    O(1)
    Space   O(1)
    Result 100/100 https://app.codility.com/demo/results/trainingFD7UYT-HG5/
"""


def solution(X, Y, D):
    # write your code in Python 3.6
    if X >= Y:
        return 0
    return (Y-X-1)//D + 1
