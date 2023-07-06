/*
    1st approach: Bfs, hashtable for visited island territories
    
    // 100 ms, faster than 12.22%
*/

/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    const R = grid.length
    const C = grid[0].length
    const seen = new Set()
    let res = 0
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (grid[i][j] === "0" || seen.has(`${i},${j}`)) {
                continue
            }
            bfs(grid, i, j, seen)
            res += 1
        }
    }
    return res
};

const bfs = (grid, x, y, seen) => {
    const R = grid.length
    const C = grid[0].length
    const q = [[x, y]]
    while (q.length > 0) {
        const [i, j] = q.shift()
        if (i < 0 || i >= R || j < 0 || j >= C) {
            continue
        }
        if (grid[i][j] === '0') {
            continue
        }
        const key = `${i},${j}`
        if (seen.has(key)) {
            continue
        }
        seen.add(key)
        q.push([i-1, j])
        q.push([i+1, j])
        q.push([i, j-1])
        q.push([i, j+1])
    }
}