def f():
    T = int(input())
    for _ in range(T):
        n, k = [int(c) for c in input().split()]
        # print(solve(n, k))
        print(solve_bsearch(n, k))


def solve(n, k):
    """
    1st: math

    tutorial: https://codeforces.com/blog/entry/77161?f0a28
    """
    return k + (k-1)//(n-1)


def solve_bsearch(n, k):
    """
    2nd: binary search
    - find the kth non-divisable by using mid - mid // n,
        where mid//n is the count of numbers divisible by n
    """
    left = 1
    right = 2**32
    while left < right:
        mid = (left + right) // 2

        non_divisable_cnt = mid - mid // n

        if k <= non_divisable_cnt:
            right = mid
        else:
            left = mid + 1
    return left


f()
