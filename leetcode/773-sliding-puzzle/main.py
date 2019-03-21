class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int

        1st approach: bfs + hashset to avoid redundant traversal

        Time    O(n!) the total number of permutation of the board states
        Space   O(n!)
        92 ms, faster than 28.41%
        """
        # to avoid vistied states
        seen = set()
        # bfs
        q = []
        q.append((board, 0))  # board, steps
        while len(q) > 0:
            b, steps = q.pop(0)

            # check if the the state is visited
            key = self.stringifyBoard(b)
            if key in seen:
                continue
            seen.add(key)

            # enqueue variations if final state not reach
            # or compare string instead of comparing the array of literals
            if b == [[1, 2, 3], [4, 5, 0]]:
                return steps
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if b[i][j] == 0:
                        if i-1 >= 0:
                            temp = self.cloneBoard(b)
                            temp[i-1][j], temp[i][j] = temp[i][j], temp[i-1][j]
                            q.append((temp, steps+1))
                        if i+1 < len(b):
                            temp = self.cloneBoard(b)
                            temp[i+1][j], temp[i][j] = temp[i][j], temp[+1][j]
                            q.append((temp, steps+1))
                        if j-1 >= 0:
                            temp = self.cloneBoard(b)
                            temp[i][j-1], temp[i][j] = temp[i][j], temp[i][j-1]
                            q.append((temp, steps+1))
                        if j+1 < len(b[0]):
                            temp = self.cloneBoard(b)
                            temp[i][j+1], temp[i][j] = temp[i][j], temp[i][j+1]
                            q.append((temp, steps+1))
        return -1

    def stringifyBoard(self, board):
        s = ""
        for i in range(len(board)):
            for j in range(len(board[i])):
                s += str(board[i][j])
        return s

    def cloneBoard(self, board):
        temp = []
        for i in range(len(board)):
            arr = []
            for j in range(len(board[i])):
                arr.append(board[i][j])
            temp.append(arr)
        return temp


# a = [[1, 2, 3], [4, 5, 0]]
# b = [[1, 2, 3], [4, 5, 0]]
# print(a == b)

print(Solution().slidingPuzzle([[1, 2, 3], [4, 0, 5]]))
print(Solution().slidingPuzzle([[1, 2, 3], [5, 4, 0]]))
print(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
print(Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
