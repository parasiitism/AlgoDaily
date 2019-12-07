"""
    1st:
    - transform to an 1D array
    - slice the array at n-k, and put 2nd half in front of the 1st half  e.g. ab -> ba
    - transform back to an 2D array

    Time    O(3N)
    Space   O(N)
    140 ms, faster than 90.54%
"""


class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        for row in grid:
            arr += row
        r, c = len(grid), len(grid[0])
        n = r*c
        k = k % n
        newArr = arr[n-k:] + arr[:n-k]
        matrix = []
        while len(newArr) > 0:
            matrix.append(newArr[:c])
            newArr = newArr[c:]
        return matrix
