from math import *

"""
    1st: O(N * sqrt(X))
    TLE
"""


# def f():
#     _ = int(input())
#     nums = [int(s) for s in input().split()]
#     for x in nums:
#         if x == 1:
#             print("NO")
#             continue
#         root = ceil(sqrt(x))
#         if root * root != x:
#             print("NO")
#         else:
#             isSingle = True
#             for i in range(2, root):
#                 if x % i == 0:
#                     print("NO")
#                     isSingle = False
#                     break
#             if isSingle:
#                 print("YES")
# f()

"""
    1st: DP, math
    - as long as the root is a prime, it is an "YES"
"""


def f():
    _ = int(input())

    nums = [int(s) for s in input().split()]

    maxInt = max(nums)
    n = ceil(sqrt(maxInt)) + 1
    dp = n*[True]
    dp[0] = False
    dp[1] = False
    primes = set()
    for i in range(2, n):
        if dp[i] == True:
            primes.add(i)
            j = 2
            while i*j < n:
                dp[i*j] = False
                j += 1
    # print(primes)
    for x in nums:
        if x == 1:
            print("NO")
        else:
            root = ceil(sqrt(x))
            if root * root == x and root in primes:
                print("YES")
            else:
                print("NO")


f()
