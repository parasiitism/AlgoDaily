"""
    2nd approach:
    - if the number of symbols are valid, there are only 2 senarios
        1. player 1 wins and the number of X == O+1
        2. player 2 wins and the number of O == X

    Time    O(n^3) -> O(1) due to n=3 as always
    Space   O(2n) -> O(1) due to n=3 as always
    20 ms, faster than 82.47%
"""


class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        n = len(board)

        nx = 0
        no = 0

        rows = n*[0]
        cols = n*[0]
        diag = 0
        antiDiag = 0

        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                toAdd = 0
                if cell == 'X':
                    nx += 1
                    toAdd = 1
                if cell == 'O':
                    no += 1
                    toAdd = -1
                rows[i] += toAdd
                cols[j] += toAdd
                if i == j:
                    diag += toAdd
                if i + j == n-1:
                    antiDiag += toAdd

        # if len no valid, return false immediately
        if nx > no + 1 or no > nx:
            return False

        player1win = False
        player2win = False

        for row in rows:
            if row == n:
                player1win = True
            if row == -n:
                player2win = True

        for col in cols:
            if col == n:
                player1win = True
            if col == -n:
                player2win = True

        if diag == n:
            player1win = True
        elif diag == -n:
            player2win = True

        if antiDiag == n:
            player1win = True
        elif antiDiag == -n:
            player2win = True

        if player1win and player2win:
            return False

        if player1win:
            if nx != no + 1:
                return False

        if player2win:
            if nx != no:
                return False

        return True


a = ["O  ", "   ", "   "]
print(Solution().validTicTacToe(a))

a = ["XOX", " X ", "   "]
print(Solution().validTicTacToe(a))

a = ["XXX", "   ", "OOO"]
print(Solution().validTicTacToe(a))

a = ["XOX", "O O", "XOX"]
print(Solution().validTicTacToe(a))

a = ["XXX", "OOX", "OOX"]
print(Solution().validTicTacToe(a))

a = ["XXX", "XOO", "OO "]
print(Solution().validTicTacToe(a))

a = ["XXO", "XOX", "OXO"]
print(Solution().validTicTacToe(a))
