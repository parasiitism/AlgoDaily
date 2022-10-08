"""
    Given 3 list of sorted arrays, merge them

    Time    O(A+B+C)
    Space   O(1)
"""


def f(A, B, C):
    res = []
    i, j, k = 0, 0, 0
    A_len, B_len, C_len = len(A), len(B), len(C)
    while i < A_len or j < B_len or k < C_len:
        mi = 2**32
        if i < A_len:
            mi = min(mi, A[i])
        if j < B_len:
            mi = min(mi, B[j])
        if k < C_len:
            mi = min(mi, C[k])
        while i < A_len and A[i] <= mi:
            res.append(A[i])
            i += 1
        while j < B_len and B[j] <= mi:
            res.append(B[j])
            j += 1
        while k < C_len and C[k] <= mi:
            res.append(C[k])
            k += 1
    return res


a = [1, 3, 6, 6, 10]
b = [-75, -20, -1, -1, 0, 2, 7]
c = [-75, -3, -3, 4, 4, 5, 6, 9, 10]

# res: [-75, -75, -20, -3, -3, -1, -1, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 9, 10, 10]
print(f(a, b, c))

print("-----")

"""
    followup: only the distinct numbers
"""


def f(A, B, C):
    res = []
    i, j, k = 0, 0, 0
    A_len, B_len, C_len = len(A), len(B), len(C)
    while i < A_len or j < B_len or k < C_len:
        mi = 2**32
        if i < A_len:
            mi = min(mi, A[i])
        if j < B_len:
            mi = min(mi, B[j])
        if k < C_len:
            mi = min(mi, C[k])
        res.append(mi)
        while i < A_len and A[i] <= mi:
            i += 1
        while j < B_len and B[j] <= mi:
            j += 1
        while k < C_len and C[k] <= mi:
            k += 1
    return res


a = [1, 3, 6, 6, 10]
b = [-75, -20, -1, -1, 0, 2, 7]
c = [-75, -3, -3, 4, 4, 5, 6, 9, 10]


# res: [-75, -20, -3, -1, 0, 1, 2, 3, 4, 5, 6, 7, 9, 10]
print(f(a, b, c))
