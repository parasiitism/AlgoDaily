/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const R = 9
    const C = 9
    // row 
    for (let i = 0; i < R; i++) {
        const hset = new Set()
        for (let j = 0; j < C; j++) {
            const x = board[i][j]
            if (x === '.') { continue }
            if (hset.has(x)) {
                return false
            }
            hset.add(x)
        }
    }
    // col
    for (let j = 0; j < R; j++) {
        const hset = new Set()
        for (let i = 0; i < C; i++) {
            const x = board[i][j]
            if (x === '.') { continue }
            if (hset.has(x)) {
                return false
            }
            hset.add(x)
        }
    }
    // grid
    const upperLefts = [
        [0,0], [0,3], [0,6],
        [3,0], [3,3], [3,6],
        [6,0], [6,3], [6,6]
    ]
    for (let [x, y] of upperLefts) {
        const hset = new Set()
        for (let i = x; i < x+3; i++) {
            for (let j = y; j < y+3; j++) {
                const x = board[i][j]
                if (x == '.') { continue }
                if (hset.has(x)) {
                    return false
                }
                hset.add(x)
            }
        }
    }

    return true
};