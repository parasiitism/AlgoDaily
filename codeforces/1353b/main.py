def f():
    T = int(input())
    for _ in range(T):
        n, k = map(int, input().split())
        A = [int(s) for s in input().split(" ")]
        B = [int(s) for s in input().split(" ")]
        A.sort()
        B.sort(key=lambda x: -x)
        i, j = 0, 0
        while k > 0 and i < n and j < n:
            if A[i] < B[j]:
                A[i] = B[j]
                i += 1
                j += 1
                k -= 1
            else:
                break
        print(sum(A))


f()
