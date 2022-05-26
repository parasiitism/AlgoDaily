def f():
    n, t = map(int, input().split())
    nums = [0] + [int(c) for c in input().split()]
    cur = 1
    while cur < t:
        cur += nums[cur]
    if cur == t:
        return "YES"
    return "NO"


print(f())
