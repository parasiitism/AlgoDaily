/*
    array

    Time    O(RC)
    Space   O(C)
*/

/**
 * @param {number[][]} grid
 * @return {number[]}
 */
var findColumnWidth = function(grid) {
    const R = grid.length
    const ht = {}
    let max_C = 0
    for (let i = 0; i < R; i++) {
        const row = grid[i]
        const C = row.length
        max_C = Math.max(max_C, C)
        for (let j = 0; j < C; j++) {
            const x = grid[i][j]
            const s = x.toString()
            const L = s.length
            if (j in ht === false) {
                ht[j] = 0
            }
            ht[j] = Math.max(ht[j], L)
        }
    }
    const res = []
    for (let c = 0; c < max_C; c++) {
        res.push(ht[c])
    }
    return res
};