"""
    Prefix sum

    idea:

    0 1 2 3 4 5 6   <- indices
    # . . . # # #   <- string
    0 0 1 1 0 1 1   <- True/False
      ^     ^
    0 0 1 2 2 3 4   <- prefix sum or True/False
    
    query(2, 5) = cache[5] - cache[2] = 3 - 1 = 2

    Time    O(N + Q)
    Space   O(N)
"""


def f():
    s = input()
    n = int(input())

    pfs = 0
    cache = [0]
    for i in range(1, len(s)):
        x = s[i-1]
        y = s[i]
        if x == y:
            pfs += 1
            cache.append(pfs)
        else:
            cache.append(pfs)

    for _ in range(n):
        l, r = map(int, input().split())
        l -= 1
        r -= 1

        print(cache[r] - cache[l])


f()
