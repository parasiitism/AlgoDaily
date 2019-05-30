"""
    1st approach: math

    Time    O(n)
    Space   O(n)
    Result 100/100 https://app.codility.com/demo/results/trainingRUEHV7-FPA/
"""


def solution(A):
    # write your code in Python 3.6
    m = set()
    for x in A:
        m.add(x)
    for i in range(1, len(A)+1):
        if i not in m:
            return i
    return len(A) + 1
