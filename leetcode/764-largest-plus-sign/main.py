"""
    1st: dynamic programming
    - make a class for cells, which contains the number of ones in 4 directions
    - store the number of ones in 4 directions

    Time    O(RC) = O(N^2)
    Space   O(RC)
    LTE     58 / 58 test cases passed, but took too long. <- WTF passed all the tests but LTE ?!?!
"""


class Cell(object):
    def __init__(self):
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None


class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        matrix = [N*[1] for _ in range(N)]
        for i, j in mines:
            matrix[i][j] = 0
        self.dp = []
        for _ in range(N):
            arr = []
            for _ in range(N):
                arr.append(Cell())
            self.dp.append(arr)

        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 1:
                    if self.dp[i][j].left == None:
                        self.count2Right(matrix, i, j)
                    if self.dp[i][j].top == None:
                        self.count2Bottom(matrix, i, j)
        res = 0
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 1:
                    order = min(
                        self.dp[i][j].top,
                        self.dp[i][j].bottom,
                        self.dp[i][j].left,
                        self.dp[i][j].right,
                    )
                    res = max(res, order)
        return res

    def count2Right(self, matrix, i, j):
        count = 0
        j_ = j
        while j_ < len(matrix[0]):
            if matrix[i][j_] == 1:
                count += 1
            else:
                break
            j_ += 1
        x = 1
        for idx in range(j, j + count):
            self.dp[i][idx].left = count - x + 1
            self.dp[i][idx].right = x
            x += 1

    def count2Bottom(self, matrix, i, j):
        count = 0
        i_ = i
        while i_ < len(matrix):
            if matrix[i_][j] == 1:
                count += 1
            else:
                break
            i_ += 1
        x = 1
        for idx in range(i, i + count):
            self.dp[idx][j].top = x
            self.dp[idx][j].bottom = count - x + 1
            x += 1


s = Solution()
a = 5
b = [[4, 2]]
print(s.orderOfLargestPlusSign(a, b))

a = 2
b = [[0, 0], [0, 1], [1, 0]]
print(s.orderOfLargestPlusSign(a, b))


"""
    2nd: dynamic programming
    - exactly the same with 1st approach, but without using OOP

    Time    O(RC) = O(N^2)
    Space   O(RC)
    4328 ms, faster than 7.50%
"""


class Solution(object):
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        # construct a matrix
        matrix = [N*[1] for _ in range(N)]
        for i, j in mines:
            matrix[i][j] = 0
        # construct a matrix with [top, bottom, left, right]
        self.dp = []
        for _ in range(N):
            arr = []
            for _ in range(N):
                arr.append([-1, -1, -1, -1])  # top, bottom, left, right
            self.dp.append(arr)
        # traverse the matrix
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 1:
                    if self.dp[i][j][0] == -1:
                        self.count2Bottom(matrix, i, j)
                    if self.dp[i][j][2] == -1:
                        self.count2Right(matrix, i, j)
        # traverse the dp matrix to find the max order
        res = 0
        for i in range(N):
            for j in range(N):
                if matrix[i][j] == 1:
                    order = min(self.dp[i][j])
                    res = max(res, order)
        return res

    def count2Right(self, matrix, i, j):
        # count the number of ones to the right
        count = 0
        j_ = j
        while j_ < len(matrix[0]):
            if matrix[i][j_] == 1:
                count += 1
            else:
                break
            j_ += 1
        # assign the number of ones to the left and to the right
        x = 1
        for idx in range(j, j + count):
            self.dp[i][idx][2] = count - x + 1
            self.dp[i][idx][3] = x
            x += 1

    def count2Bottom(self, matrix, i, j):
        # count the number of ones to the bottom
        count = 0
        i_ = i
        while i_ < len(matrix):
            if matrix[i_][j] == 1:
                count += 1
            else:
                break
            i_ += 1
        # assign the number of ones to the top and to the bottom
        x = 1
        for idx in range(i, i + count):
            self.dp[idx][j][0] = x
            self.dp[idx][j][1] = count - x + 1
            x += 1
