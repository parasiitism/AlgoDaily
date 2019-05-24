"""
    1st approach: bit op
    - get the position of each one, compare with the previous position
    - if the diff between curpos and prevpos is larger than the intermediate result, update the intermediate result

    Time    O(logn)
    Space   O(1)

    100/100
    ref: https://app.codility.com/demo/results/trainingYGTHR8-3KD/
"""


def solution(N):
    res = 0
    prev = -1
    i = 0
    while N > 0:
        if N & 1 == 1:
            if prev != -1:
                diff = i - prev - 1
                res = max(res, diff)
            prev = i
        i += 1
        N >>= 1
    return res
