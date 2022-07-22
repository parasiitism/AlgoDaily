def f():
    n = int(input())
    for _ in range(n):
        _ = input()
        nums = [int(c) for c in input().split()]
        smallest = min(nums)
        res = 0
        for x in nums:
            res += x - smallest
        print(res)


f()
