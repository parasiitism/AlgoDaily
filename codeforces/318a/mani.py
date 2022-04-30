"""
    0  1  2  3  4  5  6  7  8  9
    1, 3, 5, 7, 9, 2, 4, 6, 8, 10

    0  1  2  3  4  5  6  7  8
    1, 3, 5, 7, 9, 2, 4, 6, 8
                   1  2  3  4
"""


def f():
    n, k = map(int, input().split())
    k -= 1  # zero-indexed
    half = n/2.0
    if k < half:
        return k*2+1
    if n % 2 == 0:
        return (k - n//2 + 1) * 2
    return (k - n//2) * 2


print(f())
