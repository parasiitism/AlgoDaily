
"""
    1st approach:

    Time    
    Space   
"""


def f():
    M, N = map(int, input().split())  # R, C
    if M <= 1 and N <= 1:
        return 0
    if M == 1:
        return N//2
    if N == 1:
        return M//2
    r, r_remain = M//2, M % 2
    c, c_remain = N//2, N % 2
    a = 0
    if r_remain > 0:
        a = N//2
    b = 0
    if c_remain > 0:
        b = M//2
    return 2*r*c + a + b


print(f())
