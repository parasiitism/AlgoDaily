"""
    1st approach:
	- put all the "heads" in an array, "heads" are top boundary and right boundary of the matrix
    - iterative the head from top-left to bottom-left
	- for "head" at even indices, reverse it 
    
	Time		O(m*n)
	Space		O(m*n) the 2D array
	184 ms, faster than 33.62%
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        R, C = len(mat), len(mat[0])
        heads = []
        for j in range(C):
            heads.append((0, j))
        for i in range(1, R):
            heads.append((i, C-1))
        res = []
        for i in range(len(heads)):
            r, c = heads[i]
            arr = []
            while r < R and c >= 0:
                arr.append(mat[r][c])
                r += 1
                c -= 1
            if i % 2 == 0:
                res += arr[::-1]
            else:
                res += arr
        return res
