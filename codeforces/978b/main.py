def f():
    _ = input()
    s = input()
    res = 0
    cnt = 0
    for i in range(len(s)):
        c = s[i]
        if c == 'x':
            cnt += 1
            if cnt >= 3:
                res += 1
        else:
            cnt = 0
    print(res)


f()
