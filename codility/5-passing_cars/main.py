"""
    1st approach: prefix sum

    e.g.
    
    [0,1,0,1,1]
     3,3,2,2,1 <- prefix sum from the back

    the zero at index 0, count += 3
    the zero at index 2, count += 2

    so the answer is 5

    Time    O(n)
    Space   O(n)
    Result 100/100 https://app.codility.com/demo/results/trainingQ6467K-JVB/
"""


def solution(A):
    # write your code in Python 3.6
    prefixWesttCount = len(A) * [0]
    westCount = 0
    for i in range(len(A)-1, -1, -1):
        westCount += A[i]
        prefixWesttCount[i] = westCount
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count += prefixWesttCount[i]
    if count > 1000000000:
        return -1
    return count
