from typing import List

"""
    1st: prefix sum
    e.g.
    [
        [ 1, 2, 3, 4],
        [ 5, 6, 7, 8],
        [ 9,10,11,12],
        [13,14,15,16],
    ]
    prefix sums =
    [
        [ 1,  3,  6, 10], 
        [ 5, 11, 18, 26], 
        [ 9, 19, 30, 42], 
        [13, 27, 42, 58],
    ]

    now, u see that for every cell, pattern to calculate the block sum is
    res[i][j] += prefSums[k][i+K] - prefSums[k][i-K-1]

    then we just have to deal with the corner cases by calculating the bound of the prefSums[][]
    i.e. i+K, i-K, j-K, j+K

    Time    O(RC * 2K)
    Space   O(RC)
    452 ms, faster than 14.16%
"""


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        prefSums = [c * [0] for _ in range(r)]
        for i in range(r):
            prevSum = 0
            for j in range(c):
                prevSum += mat[i][j]
                prefSums[i][j] = prevSum
        print(prefSums)
        res = [c * [0] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                top = max(0, i-K)
                bottom = min(r-1, i+K)
                left = max(0, j-K)
                right = min(c-1, j+K)
                for k in range(top, bottom+1):
                    leftSum = 0
                    if left-1 >= 0:
                        leftSum = prefSums[k][left-1]
                    res[i][j] += prefSums[k][right] - leftSum
        return res


s = Solution()
a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
print(s.matrixBlockSum(a, 1))
