
def f():
    s = input()
    if len(s) == 0:
        return 'NO'
    d = []
    cnt = 1
    for i in range(1, len(s)):
        prev = s[i-1]
        cur = s[i]
        if prev != cur:
            d.append((prev, cnt))
            cnt = 0
        cnt += 1
    d.append((s[-1], cnt))
    for i in range(1, len(d)):
        if d[i-1][1] >= 7:
            return 'YES'
    for i in range(len(d)-2, -1, -1):
        if d[i+1][1] >= 7:
            return 'YES'
    return 'NO'


print(f())
