/*
    2nd approach
	- iterative bfs
	- when we see an one, bfs its neightbours to calculate its area and compare to the potential result
	- if it is larger than the potential result, set it as the potential result

	Time    O(n)
	Space   O(n) hashtable
	152 ms, faster than 15.95%
*/
var maxAreaOfIsland = function(grid) {
    const R = grid.length
    const C = grid[0].length
    const seen = new Set()
    let res = 0
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (grid[i][j] === 1 && seen.has(`${i},${j}`) === false) {
                const area = bfs(grid, i, j, seen)
                res = Math.max(res, area)
            }
        }
    }
    return res
};

const bfs = (grid, x, y, seen) => {
    const R = grid.length
    const C = grid[0].length
    let res = 0
    const q = [[x, y]]
    while (q.length > 0) {
        const [i, j] = q.shift()
        if (i < 0 || i >= R || j < 0 || j >= C) {
            continue
        }
        if (grid[i][j] != 1) {
            continue
        }
        const key = `${i},${j}`
        if (seen.has(key)) {
            continue
        }
        seen.add(key)
        res += 1
        q.push([i-1, j])
        q.push([i+1, j])
        q.push([i, j-1])
        q.push([i, j+1])
    }
    return res
}