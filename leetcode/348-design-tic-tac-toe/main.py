class TicTacToe(object):

    def __init__(self, n):
        self.n = n
        self.rows = n*[0]
        self.cols = n*[0]
        self.diag = 0
        self.antiDiag = 0

    def move(self, row, col, player):
        """
        2nd approach: 
        1. save player1 as +1, save player2 as -1 for each rowcount, colcount, diagonal count, antidiagonal count
        2. when any entity reach N, the player wins the game

        Time    O(1)
        Space   O(n*n)
        44 ms, faster than 84.21%
        26feb2019
        """
        toAdd = 1 if player == 1 else -1
        self.rows[row] += toAdd
        self.cols[col] += toAdd
        if row == col:
            self.diag += toAdd
        if row + col == self.n-1:
            self.antiDiag += toAdd
        if abs(self.rows[row]) == self.n \
                or abs(self.cols[col]) == self.n \
                or abs(self.diag) == self.n \
                or abs(self.antiDiag) == self.n:
            return player
        return 0
