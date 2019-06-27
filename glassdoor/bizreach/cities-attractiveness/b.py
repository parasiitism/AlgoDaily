import sys

"""
    1st: brute force

    Time    O(n^2)
    Space   O(1)
"""


def solution(A):
    # write your code in Python 3.6
    res = -sys.maxsize
    for i in range(len(A)):
        maxNow = A[i] * 2
        for j in range(i+1, len(A)):
            temp = A[i] + A[j] + j - i
            maxNow = max(maxNow, temp)
            res = max(res, maxNow)
    return res


a = [1, 3, -3]
print(solution(a))

a = [-8, 4, 0, 5, -3, 6]
print(solution(a))

print("-----")

"""
    2nd: dynamic programming 
    - similar to lc1014

    Time    O(n)
    Space   O(1)
"""


def solution(A):
    prevBest = 0
    res = 0
    for i in range(len(A)):
        res = max(res, prevBest+A[i], A[i]*2)
        # increment the prevBest when we go forward
        # A[i] + A[j] + |i - j| = (A[i] + diff) + A[j]
        prevBest = max(prevBest, A[i]) + 1
    return res


a = [1, 3, -3]
print(solution(a))

a = [-8, 4, 0, 5, -3, 6]
print(solution(a))
