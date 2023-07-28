/**
 * @param {number[][]} grid
 * @return {number}
 */
var largestIsland = function(grid) {
    const R = grid.length
    const C = grid[0].length
    const mapping = new Map() // (i,j): islandID 
    const islandsArea = new Map() // islandID: area
    let res = 0
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (grid[i][j] === 1 && mapping.has(`${i},${j}`) === false) {
                const islandID = islandsArea.size
                const area = bfs(grid, i, j, mapping, islandID)
                islandsArea.set(islandID, area)
                res = Math.max(res, area)
            }
        }
    }
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (grid[i][j] != 0) {
                continue
            }
            const dirs = [[-1,0],[1,0],[0,-1],[0,1]]
            const islands = new Set()
            for (let [di, dj] of dirs) {
                const x = i+di
                const y = j+dj
                if (x < 0 || x >= R || y < 0 || y >= C) {
                    continue
                }
                const key = `${x},${y}`
                if (mapping.has(key)) {
                    const islandID = mapping.get(key)
                    islands.add(islandID)
                }
            }
            let total = 1
            islands.forEach(id => {
                total += islandsArea.get(id)
            })
            res = Math.max(res, total)
        }
    }
    return res
};


const bfs = (grid, x, y, mapping, islandID) => {
    const R = grid.length
    const C = grid[0].length
    let area = 0
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
        if (mapping.has(key)) {
            continue
        }
        mapping.set(key, islandID)
        area += 1
        q.push([i-1, j])
        q.push([i+1, j])
        q.push([i, j-1])
        q.push([i, j+1])
    }
    return area
}