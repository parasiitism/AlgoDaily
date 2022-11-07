def f():
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = [int(c) for c in input().split()]
        print(solve(arr))


def solve(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i-1] >= arr[i]:
            return "NO"
    return "YES"


f()
