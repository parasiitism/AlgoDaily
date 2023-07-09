def print_pattern(matrix, n):

    L = len(matrix)

    for _ in range(n-1):

        M = len(matrix) * L
        new_matrix = [[False] * M for _ in range(M)]

        for r in range(len(matrix)):
            for c in range(len(matrix)):
                if matrix[r][c] == False:
                    continue
                for r2 in range(L):
                    for c2 in range(L):
                        new_matrix[r*L+r2][c*L+c2] = matrix[r2][c2]
        matrix = new_matrix

    for row in matrix:
        s = ''
        for x in row:
            if x:
                s += 'X'
            else:
                s += ' '
        print(s)


a = [[True, True, True], [True, False, True], [True, True, True]]
b = 1
print(print_pattern(a, b))

a = [[True, True, True], [True, False, True], [True, True, True]]
b = 2
print(print_pattern(a, b))

a = [[True, True, True], [True, False, True], [True, True, True]]
b = 3
print(print_pattern(a, b))

print("-----")

a = [[True, True, True], [True, False, False], [True, False, False]]
b = 1
print(print_pattern(a, b))

a = [[True, True, True], [True, False, False], [True, False, False]]
b = 2
print(print_pattern(a, b))

a = [[True, True, True], [True, False, False], [True, False, False]]
b = 3
print(print_pattern(a, b))
