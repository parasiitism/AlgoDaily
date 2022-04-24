
def f():
    T = int(input())
    for _ in range(T):
        n = int(input())
        nums = [int(s) for s in input().split(" ")]
        nums.sort()
        res = 2**32
        for i in range(1, n):
            diff = nums[i] - nums[i-1]
            res = min(res, diff)
        print(res)


f()
