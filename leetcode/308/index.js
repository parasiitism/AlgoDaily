/*
    Binary Index Tree
    - create BIT on each row
    - when we query, use BIT range query to fast compute the sum from col1 to col2

    Time of update()    O(logC)
    Time of sumRange()  O(RlogC)
    Runtime 280 ms Beats 82.3%
*/
class BIT {
    constructor(n) {
        this.A = Array(n+1).fill(0)
    }
    update(i, val) {
        let j = i+1
        while (j < this.A.length) {
            this.A[j] += val
            j += j & -j
        }
    }
    sum(i) {
        let total = 0
        let j = i+1
        while (j > 0) {
            total += this.A[j]
            j -= j & -j
        }
        return total
    }
    sumBetween(left, right) {
        return this.sum(right) - this.sum(left-1)
    }
}

class NumMatrix {
    constructor(matrix) {
        this.matrix = matrix
        const R = matrix.length
        const C = matrix[0].length
        this.BITs = []
        for (let i = 0; i < R; i++) {
            let bit = new BIT(C)
            for (let j = 0; j < C; j++) {
                bit.update(j, matrix[i][j])
            }
            this.BITs.push(bit)
        }
    }
    update(row, col, val) {
        const oldVal = this.matrix[row][col]
        const diff = val - oldVal
        this.BITs[row].update(col, diff)
        this.matrix[row][col] = val
    }
    sumRegion(row1, col1, row2, col2) {
        let total = 0
        for (let i = row1; i <= row2; i++) {
            const bit = this.BITs[i]
            total += bit.sumBetween(col1, col2)
        }
        return total
    }
}

/** 
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * obj.update(row,col,val)
 * var param_2 = obj.sumRegion(row1,col1,row2,col2)
 */