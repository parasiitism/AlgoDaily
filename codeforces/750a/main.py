def f():
    n, k = [int(x) for x in input().split()]
    t = 240 - k
    pfs = 0
    count = 0
    for i in range(1, n+1):
        pfs += i*5
        if pfs > t:
            break
        count += 1
    return count


print(f())
