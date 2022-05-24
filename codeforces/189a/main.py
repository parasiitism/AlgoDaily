"""
    Dynamic programming
    - backpack problem
    - try cutting the ribbon with all integers 0 - N

    https://icode.best/i/40732646351591
"""


def f():
    n, a, b, c = map(int, input().split())
    w = [a, b, c]
    dp = [0] + [-1] * n
    for i in range(3):
        sub = w[i]
        for j in range(sub, n + 1):
            if dp[j - sub] != -1:
                dp[j] = max(dp[j], dp[j - sub] + 1)
    return dp[n]


print(f())
