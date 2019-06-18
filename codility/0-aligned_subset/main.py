"""
Given an array A and integer M, find a subset that the distance between any two numbers within the subset is divisible by M. 
Your task is to find the size of the largest subset.

e.g.1
A = [3, -2, 1, 0, 8, 7, 1], M = 3

The result = 4, because any diff between 2 numbers in the subset [-2, 1, 7, 1] is divisible by 3

e.g.2
A = [3, -2, 1, 0, 8, 7, 1, 4], M = 3

The result = 5, because any diff between 2 numbers in the subset [-2, 1, 7, 1, 4] is divisible by 3

e.g.3
A = [7, 1, 11, 8, 4, 10], M = 8
The result = 1, because [8] is divisible by 8 and no other subsets which diff between any pairs is divisible by 8

Time    O(n)
Space   O(n)
"""


def solution(A, M):
    m = {}
    for i in range(len(A)):
        num = A[i]
        mod = num % M
        # in python -2%3 = 1
        # if mod != 0 and mod < 0:
        #     mod = mod + M
        if mod not in m:
            m[mod] = 1
        else:
            m[mod] += 1
    res = 0
    for key in m:
        res = max(res, m[key])
    return res


A = [3, -2, 1, 0, 8, 7, 1]
M = 3
print(solution(A, M))

A = [3, -2, 1, 0, 8, 7, 1, 4]
M = 3
print(solution(A, M))

A = [3, -2, 1, 0, 8, 7, 1, 4, -5]
M = 3
print(solution(A, M))

A = [7, 1, 11, 8, 4, 10]
M = 8
print(solution(A, M))
