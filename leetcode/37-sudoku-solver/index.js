/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solveSudoku = function(board) {
    const N = board.length

    const createSets = n => {
        const res = []
        for (let i = 0 ; i < n; i++) { res.push(new Set()); }
        return res
    }
    const ht_row = createSets(N)
    const ht_col = createSets(N)
    const ht_region = createSets(N) // 0:(0,0), 1:(0,3), 2:(0,6), 3:(3,0), 4:(3,3)...

    const original = []
    for (let i = 0; i < N; i++) {
        const row = []
        for (let j = 0; j < N; j++) {
            const ij = Math.floor(i/3)*3 + Math.floor(j/3)
            const x = board[i][j]
            row.push(x)
            if (x === '.') {
                continue
            }
            ht_row[i].add(x)
            ht_col[j].add(x)
            ht_region[ij].add(x)
        }
        original.push(row)
    }

    const backtrack = (i, j) => {
        if (i === N && j === 0) {
            return true
        }
        if (original[i][j] != '.') {
            let b = false
            if (j+1 < N) {
                b = backtrack(i, j+1)
            } else {
                b = backtrack(i+1, 0)
            }
            return b
        }
        
        const ij = Math.floor(i/3)*3 + Math.floor(j/3)
        const cands = []
        for (let x = 1; x <= N; x++) {
            const c = `${x}`
            if (ht_row[i].has(c) || ht_col[j].has(c) || ht_region[ij].has(c)) {
                continue
            }
            cands.push(c)
        }
        
        for (let c of cands) {
            board[i][j] = c
            ht_row[i].add(c)
            ht_col[j].add(c)
            ht_region[ij].add(c)
            let b = false
            if (j+1 < N) {
                b = backtrack(i, j+1)
            } else {
                b = backtrack(i+1, 0)
            }
            if (b) {
                return true
            }
            ht_row[i].delete(c)
            ht_col[j].delete(c)
            ht_region[ij].delete(c)
            board[i][j] = '.'
        }
        return false
    }
    backtrack(0, 0)
};