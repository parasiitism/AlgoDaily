def f():
    s = input()
    x = int(s)
    y = int(s[:-1])
    z = int(s[:-2] + s[-1])
    print(max(x, y, z))


f()
