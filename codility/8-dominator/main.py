"""
    similar to lc961

    Time    O(n)
    Space   O(n)
    Result 100/100 https://app.codility.com/demo/results/trainingFRBBYC-S8P/
"""


def solution(A):
    # write your code in Python 3.6
    ht = {}
    for i in range(len(A)):
        num = A[i]
        if num not in ht:
            ht[num] = 1
        else:
            ht[num] += 1
        if ht[num] > len(A)//2:
            return i
    return -1
