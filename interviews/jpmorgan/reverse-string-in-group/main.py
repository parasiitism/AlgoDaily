"""
    Reverse string/items in group of size K
    - put the characters in a temporary group
    - if the length of the temp == K, reverse it and append to the result
    - finally if there are still some characters not being reversed, put them the result with original order

    https://www.1point3acres.com/bbs/thread-282628-1-1.html
"""


def f(S, K):
    res = ""
    cur = ""
    for i in range(len(S)):
        c = S[i]
        cur += c
        if len(cur) == K:
            res += cur[::-1]
            cur = ""
    if len(cur) > 0:
        res += cur
    return res


a = "abcdefghijklm"
b = 3
print(f(a, b))

a = "abcdef"
b = 3
print(f(a, b))
