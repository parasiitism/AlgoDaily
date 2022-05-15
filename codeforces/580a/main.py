def f():
    N = int(input())
    nums = [int(s) for s in input().split()]
    res = 1
    j = 0
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            j = i
        else:
            res = max(res, i - j + 1)
    return res


print(f())
