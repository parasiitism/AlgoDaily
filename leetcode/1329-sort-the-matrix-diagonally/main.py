"""
    1st: sort
    - get the left + up boundaries
    - iterate from each boundary diagonally and put the numbers into array
    - sort the array and put that into a temporary array
    - put the numbers back in

    Time    O(NlogN)
    Space   O(N)
    76 ms, faster than 72.33%
"""


class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(mat), len(mat[0])
        starts = []
        for i in range(r-1, -1, -1):
            starts.append((i, 0))
        for i in range(1, c):
            starts.append((0, i))

        diags = []
        for x, y in starts:
            arr = []
            i, j = x, y
            while i < r and j < c:
                arr.append(mat[i][j])
                i += 1
                j += 1
            diags.append(sorted(arr))

        for x, y in starts:
            i, j = x, y
            cur = diags.pop(0)
            while i < r and j < c:
                mat[i][j] = cur.pop(0)
                i += 1
                j += 1
        return mat
