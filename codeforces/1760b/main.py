def f():
    T = int(input())
    for _ in range(T):
        _ = input()
        s = input()
        max_idx = 0
        for c in s:
            idx = ord(c) - ord('a')
            max_idx = max(max_idx, idx)
        print(max_idx+1)


f()
