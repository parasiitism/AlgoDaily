class Solution:
    """
    By Dale
    """

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if rows == 0:
            return []
        cols = len(matrix[0])
        output = []
        for edge in range(0, min((cols+1) // 2, (rows+1) // 2)):
            # top-left -> top-right
            for x in range(edge, cols-edge):
                output.append(matrix[edge][x])

            # top-right w/o corner -> bottom-right
            for y in range(edge+1, rows-edge):
                output.append(matrix[y][cols-edge-1])

            # bottom-right w/o corner -> bottom-left
            if edge < rows-edge-1:
                for x in range(cols-edge-2, edge-1, -1):
                    output.append(matrix[rows-edge-1][x])

            # bottom-left w/o corner -> top-left w/o corner
            if edge < cols-edge-1:
                for y in range(rows-edge-2, edge, -1):
                    output.append(matrix[y][edge])
        return output


s = Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(s)
