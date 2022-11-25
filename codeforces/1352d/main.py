"""
    2 pointers

    Time    O(N) 202 ms
    Space   O(1) 200 KB
"""


def f():
    T = int(input())
    for _ in range(T):
        _ = input()
        nums = [int(c) for c in input().split()]
        solve(nums)


def solve(nums):
    n = len(nums)
    i, j = -1, n
    a, b = 0, 0
    cur_max_size = 0
    is_left = True
    cnt = 0
    while i+1 < j:
        if is_left:
            size = 0
            while i+1 < j and size <= cur_max_size:
                size += nums[i+1]
                i += 1
            a += size
            cur_max_size = size
            is_left = False
            cnt += 1
        else:
            size = 0
            while i < j-1 and size <= cur_max_size:
                size += nums[j-1]
                j -= 1
            b += size
            cur_max_size = size
            is_left = True
            cnt += 1
    print(cnt, a, b)


# solve([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
# solve([1000])
# solve([1, 1, 1])
# solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
# solve([2, 1])
# solve([1, 1, 1, 1, 1, 1])
# solve([1, 1, 1, 1, 1, 1, 1])

f()
