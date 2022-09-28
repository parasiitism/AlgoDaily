def f():
    _ = input()
    nums = [int(c) for c in input().split()]
    n = len(nums)
    dp = n * [1]
    for i in range(1, n):
        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1] + 1
    print(max(dp))


f()
