def f():
    n = int(input())
    for _ in range(n):
        angle = int(input())
        sides = 360.0 / (180.0 - angle)
        if int(sides) == sides:
            print("YES")
        else:
            print("NO")


f()
