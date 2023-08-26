const abs = Math.abs

class TicTacToe {
    constructor(n) {
        this.n = n
        this.rows = Array(n).fill(0)
        this.cols = Array(n).fill(0)
        this.diag = 0       // i,j; i+1, j+1
        this.antiDiag = 0   // i+j == n-1
    }
    move(i, j, player) {
        const n = this.n
        let score = 0
        if (player == 2) {
            score = -1
        } else {
            score = 1
        }
        this.rows[i] += score
        this.cols[j] += score
        if (i == j) {
            this.diag += score
        }
        if (i+j+1 == n) {
            this.antiDiag += score
        }
        if (
            abs(this.rows[i]) == n || abs(this.cols[j]) == n 
            || abs(this.diag) == n || abs(this.antiDiag) == n
        ) {
            return player
        }
        return 0
    }
}

/**
 * Your TicTacToe object will be instantiated and called as such:
 * var obj = new TicTacToe(n)
 * var param_1 = obj.move(row,col,player)
 */
