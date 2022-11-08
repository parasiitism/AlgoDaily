from collections import *


def f():
    T = int(input())
    for _ in range(T):
        _space = input()
        matrix = []
        for _ in range(8):
            row = input()
            matrix.append(row)
        last = solve(matrix)
        if last is not None:
            print(last)


def solve(matrix):
    for i in range(8):
        red = 0
        for j in range(8):
            c = matrix[i][j]
            if c == 'R':
                red += 1
        if red == 8:
            return 'R'

    for j in range(8):
        blue = 0
        for i in range(8):
            c = matrix[i][j]
            if c == 'B':
                blue += 1
        if blue == 8:
            return 'B'
    return None


f()
