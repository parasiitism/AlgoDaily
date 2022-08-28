def f():
    n, m = [int(c) for c in input().split()]
    nums = [int(c) for c in input().split()]
    nums = sorted(nums)
    res = 0
    pfs = 0
    for i in range(min(m, n)):
        pfs += nums[i]
        res = max(res, -pfs)
    print(res)


f()
