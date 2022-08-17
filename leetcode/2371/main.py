"""
    heap
    - on each row&col, the smallest value starts from 1, 2, 3
    - we use a minheap to assign the new value into every cell 1 by 1
        using new_cell_value = max(min_row_vals[i], min_col_vals[j]) + 1
    
    Time    O(RC logRC)
    Space   O(RC)
    2240 ms, faster than 100.00%
"""


class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])

        min_row_vals = R * [0]
        min_col_vals = C * [0]

        cells = []
        res = []
        for i in range(R):
            temp = []
            for j in range(C):
                heapq.heappush(cells, (grid[i][j], i, j))
                temp.append(0)
            res.append(temp)

        while len(cells) > 0:
            v, i, j = heapq.heappop(cells)

            # calculate the smallest changed value for this position
            new_cell_value = max(min_row_vals[i], min_col_vals[j]) + 1
            res[i][j] = new_cell_value

            # update the two lists
            min_row_vals[i] = new_cell_value
            min_col_vals[j] = new_cell_value

        return res
