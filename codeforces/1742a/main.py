def f():
    T = int(input())
    for _ in range(T):
        arr = [int(c) for c in input().split()]
        arr.sort()
        if arr[0] + arr[1] == arr[2]:
            print("YES")
        else:
            print("NO")


f()
