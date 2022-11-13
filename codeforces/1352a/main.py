def f():
    T = int(input())
    for _ in range(T):
        n = int(input())
        res = []
        tenth = 1
        while n > 0:
            d = n % 10
            n //= 10
            if d * tenth > 0:
                res.append(d * tenth)
            tenth *= 10
        print(len(res))
        print(' '.join([str(x) for x in res]))


f()
