def f():
    s = input()
    cnt = 0
    for c in s:
        d = int(c)
        if d == 4 or d == 7:
            cnt += 1
    if cnt == 4 or cnt == 7:
        print('YES')
    else:
        print('NO')


f()
