/*
    2nd: BFS

    Time    O(2n)
    Space   O(n) hashtable
    176 ms, faster than 6.93%
*/
/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    const R = board.length
    const C = board[0].length
    const seen = new Set()
    for (let i = 0; i < R; i++) { 
        for (let j = 0; j < C; j++) {
            if (board[i][j] == 'X' || seen.has(`${i},${j}`)) {
                continue
            }
            const [isSurroundedByX, traversed] = bfs(board, i, j)
            if (isSurroundedByX) {
                traversed.forEach(key => {
                    const [r, c] = key.split(',')
                    board[r][c] = 'X'
                })
            } else {
                traversed.forEach(key => {
                    seen.add(key)
                })
            }
        }
    }
};

const bfs = (board, x, y) => {
    const R = board.length
    const C = board[0].length
    
    const q = [[x, y]]
    let isSurroundedByX = false
    let isSurroundedByBoundary = false
    const seen = new Set()
    while (q.length > 0) {
        const [i, j] = q.shift()
        if (i < 0 || i >= R || j < 0 || j >= C) {
            isSurroundedByBoundary = true
            continue
        }
        if (board[i][j] === 'X') {
            isSurroundedByX = true
            continue
        }
        const key = `${i},${j}`
        if (seen.has(key)) {
            continue
        }
        seen.add(key)
        q.push([i-1,j])
        q.push([i+1,j])
        q.push([i,j-1])
        q.push([i,j+1])
    }
    return [
        isSurroundedByX && !isSurroundedByBoundary,
        seen
    ]
}
