def f():
    T = int(input())
    for _ in range(T):
        s = input()
        idx = solve(s)
        print(idx + 1)


def solve(s):
    n = len(s)
    A_min, A_max = 0, 0
    B_min, B_max = 0, 0
    for i in range(n):
        c = 0
        try:
            c = int(s[i])
        except:
            pass
        if i % 2 == 0:
            A_min += c
            if s[i] == '?':
                A_max += 1
            else:
                A_max += c
        else:
            B_min += c
            if s[i] == '?':
                B_max += 1
            else:
                B_max += c
        A_remain = 5 - (i+2) // 2
        B_remain = 5 - (i+1) // 2
        if A_max > B_min + B_remain:
            return i
        if B_max > A_min + A_remain:
            return i
    return 9


# print(solve("1?0???1001"))
# print(solve("1111111111"))
# print(solve("??????????"))
# print(solve("0100000000"))

f()
