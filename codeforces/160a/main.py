def f():
    _ = int(input())
    arr = [int(s) for s in input().split(" ")]
    total = sum(arr)
    arr.sort(key=lambda x: -x)
    pfs = 0
    for i in range(len(arr)):
        pfs += arr[i]
        if pfs > total - pfs:
            return i+1
    return i


print(f())
