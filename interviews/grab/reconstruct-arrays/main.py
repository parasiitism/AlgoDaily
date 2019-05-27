def solution(U, L, C):
    # write your code in Python 3.6
    a = len(C) * [0]
    for i in range(len(C)):
        if C[i] > 0 and U > 0:
            a[i] = 1
            U -= 1
            C[i] -= 1
    if U > 0:
        return "IMPOSSIBLE"
    countOneInC = 0
    for item in C:
        countOneInC += item
    if countOneInC != L:
        return "IMPOSSIBLE"
    return "".join([str(x) for x in a]) + "," + "".join([str(x) for x in C])


print(solution(3, 2, [2, 1, 1, 0, 1]))
