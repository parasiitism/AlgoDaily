"""
    https://github.com/htoma/codility/blob/master/codility/Code/Countries.cs

    Given a matrix NxM where each cell has a color indicator, count the number of distinct countries
    where a country is a group of same-color cells and neighboring is performed on the 4 directions: N-E-S-W

    Time    O(MN)
    Space   O(MN)
"""


def f(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0
    seen = set()
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) not in seen:
                dfs(matrix, i, j, seen, matrix[i][j])
                count += 1
    return count


def dfs(matrix, i, j, seen, lastColor):
    if i < 0 or i+1 > len(matrix) or j < 0 or j+1 > len(matrix[0]):
        return
    if matrix[i][j] == lastColor:
        if (i, j) in seen:
            return
        seen.add((i, j))
        dfs(matrix, i-1, j, seen, lastColor)
        dfs(matrix, i+1, j, seen, lastColor)
        dfs(matrix, i, j-1, seen, lastColor)
        dfs(matrix, i, j+1, seen, lastColor)


a = [
    ['a', 'a', 'b', 'b', 'c'],
    ['a', 'd', 'b', 'b', 'c'],
    ['d', 'd', 'd', 'a', 'c'],
    ['a', 'a', 'b', 'b', 'c'],
]
print(f(a))
