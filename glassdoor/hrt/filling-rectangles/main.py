def f(M):
    res_max = 0
    res_min = 0
    fisrt_indices = []
    # find max
    for row in M:
        first_block_idx = find_the_first_block(row)
        fisrt_indices.append(first_block_idx)
        res_max += first_block_idx

    # find min
    n = len(fisrt_indices)
    decreasing = n * [0]
    cur_min = len(M[0])
    for i in range(n):
        cur_min = min(cur_min, fisrt_indices[i])
        decreasing[i] = cur_min
        if cur_min == 0:  # corner-case where, a block blocks the rest of a row e.g. second row of example1
            cur_min = len(M[0])
    res_min = sum(decreasing)
    return (res_min, res_max)


def find_the_first_block(row):
    j = 0
    while j < len(row) and row[j] == '.':
        j += 1
    return j


a = [
    ['.', '#', '#'],
    ['#', '.', '.'],
    ['.', '.', '.'],
]
print(f(a))

a = [
    ['.', '#', '#'],
    ['.', '.', '#'],
    ['.', '.', '.'],
]
print(f(a))
