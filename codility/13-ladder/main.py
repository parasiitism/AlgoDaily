"""
    1st approach: bottom up dp + iteration
    - get all the fibs
    - for each item in A, dp[i]%B[i] to get the answer

    Time    O(L+A)
    Space   O(n)
    Result 87/100 https://app.codility.com/demo/results/training9HK2NZ-VBD/
"""


def solution(A, B):
    # write your code in Python 3.6
    dp = [1, 1]
    for i in range(2, 50001):
        dp.append(dp[i-1]+dp[i-2])
    # cal A
    res = []
    for i in range(len(A)):
        a = A[i]
        temp = dp[a] % (2**B[i])
        res.append(temp)
    return res
