
def f():
    _ = int(input())
    nums = [int(x) for x in input().split()]
    ma = nums[0]
    mi = nums[0]
    res = 0
    for i in range(len(nums)):
        x = nums[i]
        if x > ma:
            ma = x
            res += 1
        if x < mi:
            mi = x
            res += 1
    return res


print(f())
