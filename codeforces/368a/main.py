def f():
    n, d = map(int, input().split())
    costs = [int(x) for x in input().split()]
    m = int(input())

    res = 0
    costs.sort()
    for i in range(len(costs)):
        res += costs[i]
        m -= 1
        if m == 0:
            break
    print(res - m * d)


f()
