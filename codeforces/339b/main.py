
def f():
    n, m = map(int, input().split())
    arr = [int(s) for s in input().split(" ")]
    res = 0
    cur = 1
    for x in arr:
        if x >= cur:
            res += x - cur
            cur = x
        else:
            res += n - cur + 1
            cur = 1
            res += x - cur
            cur = x
    return res


print(f())
