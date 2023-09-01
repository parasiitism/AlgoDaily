"""
    Given 2 integer arrays, return the longest common subarray(s) amongest them. If there are more than 1 subarray, return all

    e.g.1
    A = [1,2,3,9,9,9,11,12,100,101]
    B = [4,4,4,1,2,3,99,100,101]
    
    Output = [[1,2,3]]

    e.g.2
    A = [1,2,3,9,9,9,11,12,13,100,101]
    B = [11,12,13,4,4,4,1,2,3,99,100,101]
    
    Output = [[1,2,3], [11,12,13]]

    Time    O(AB * sqrt(0.25A^2 + 0.25B^2))
    Space   O(AB)
"""
def f(A, B):
    R, C = len(A), len(B)
    cache = []
    for i in range(R+1):
        cache.append((C+1) * [0])
    max_len = 0
    for i in range(R):
        for j in range(C):
            if A[i] == B[j]:
                cache[i+1][j+1] = cache[i][j] + 1
                max_len = max(max_len, cache[i+1][j+1])
    res = []
    for i in range(R+1):
        for j in range(C+1):
            if cache[i][j] != max_len:
                continue
            path = []
            x, y = i, j
            while cache[x][y] > 0:
                path.append(A[x-1])
                x -= 1
                y -= 1
            res.append(path[::-1])
    return res

a = [1,2,3,9,9,9,11,12,13,100,101]
b = [11,12,13,4,4,4,1,2,3,99,100,101]
print(f(a, b))
