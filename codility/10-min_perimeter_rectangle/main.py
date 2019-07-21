import math

"""
    1st approach: math

    Time    O(sqrt(N))
    Space   O(1)
    Result 100/100
    https://app.codility.com/demo/results/training96RPGQ-5K6/
"""


def solution(N):
    # write your code in Python 3.6
    root = int(math.sqrt(N))
    for i in range(root+1, 0, -1):
        quotient = N//i
        if i*quotient == N:
            return 2*(i+quotient)
