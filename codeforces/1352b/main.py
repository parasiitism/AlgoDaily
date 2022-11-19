def f():
    T = int(input())
    for _ in range(T):
        n, k = [int(c) for c in input().split()]

        remain = n - (k-1)
        if remain > 0 and remain % 2 == 1:
            res = (k - 1)*[1] + [remain]
            print("YES")
            print(' '.join([str(c) for c in res]))
            continue
        
        remain = n - 2 * (k-1)
        if remain > 0 and remain % 2 == 0:
            res = (k - 1)*[2] + [remain]
            print("YES")
            print(' '.join([str(c) for c in res]))
            continue

        print("NO")

f()

        
