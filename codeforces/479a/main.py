def f():
    a = int(input())
    b = int(input())
    c = int(input())

    res = 0

    res = max(res, a + b + c)
    res = max(res, a * b * c)

    res = max(res, a + b * c)
    res = max(res, a * b + c)

    res = max(res, (a + b) * c)
    res = max(res, a * (b + c))

    return res


print(f())
