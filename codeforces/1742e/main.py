def f():
    T = int(input())
    for _ in range(T):
        input()
        steps = [int(c) for c in input().split()]
        queries = [int(c) for c in input().split()]
        heights = solve(steps, queries)
        print(' '.join([str(h) for h in heights]))


"""
    binary search, prefix sum, running max

    Time    O(S+S+QlogS)    1778 ms
    Space   O(S)             31300 KB
"""


def solve(steps, queries):
    n = len(steps)

    cur_max_step = 0                # running max
    reachable_heights = {}          # {running max: prefix sum}
    pfs = 0
    for i in range(n):
        s = steps[i]
        cur_max_step = max(cur_max_step, s)
        pfs += s
        if cur_max_step not in reachable_heights:
            reachable_heights[cur_max_step] = 0
        reachable_heights[cur_max_step] = pfs

    # prepare for binary search
    pairs = []
    keys = list(reachable_heights.keys())
    keys.sort()
    for k in keys:
        pairs.append([k, reachable_heights[k]])

    # binary search the max height for a Query can reach
    res = []
    for q in queries:
        idx = upper_bsearch(pairs, q) - 1
        if idx < 0:
            res.append(0)
        else:
            h = pairs[idx][1]
            res.append(h)
    return res


def upper_bsearch(pairs, q):
    left = 0
    right = len(pairs)
    while left < right:
        mid = (left + right) // 2
        if q >= pairs[mid][0]:
            left = mid + 1
        else:
            right = mid
    return left


# a = [1, 2, 1, 5]
# b = [1, 2, 4, 9, 10]
# print(solve(a, b))

# a = [1, 1]
# b = [0, 1]
# print(solve(a, b))

# a = [1000000000, 1000000000, 1000000000]
# b = [1000000000]
# print(solve(a, b))

f()
