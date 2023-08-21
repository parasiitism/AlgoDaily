/*
    1st approach: BFS + hastable
    - similar to lc286: walls and gates
    - on each cell
        - sum up all the steps from each buildings
        - record the number of buildings which can access this cell
    - find the min

    Time    O(kRRCC) k: number of buildings
    Space   O(2RC)
    348 ms, faster than 46.81% 
*/
var shortestDistance = function(grid) {
    const R = grid.length
    const C = grid[0].length
    
    const dists = []
    const visitCounts = []
    for (let i = 0; i < R; i++) {
        dists.push(Array(C).fill(0))
        visitCounts.push(Array(C).fill(0))
    }

    let buildingCount = 0
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (grid[i][j] == 1) {
                buildingCount += 1
                bfs(grid, i, j, dists, visitCounts)
            }
        }
    }
    let smallest = 2**32
    for (let i = 0; i < R; i++) {
        for (let j = 0; j < C; j++) {
            if (grid[i][j] == 0 && visitCounts[i][j] == buildingCount) {
                smallest = Math.min(smallest, dists[i][j])
            }
        }
    }
    return smallest != 2**32 ? smallest : -1
};

const bfs = (grid, x, y, dists, visitCounts) => {
    const R = grid.length
    const C = grid[0].length

    const seen = new Set()
    const q = [[x, y, 0]]
    while (q.length > 0) { 
        const [i, j, steps] = q.shift()
        if (i < 0 || i >= R || j < 0 || j >= C)
            continue

        if (grid[i][j] === 0 || (i == x && j == y)) {
            const key = `${i},${j}`
            if (seen.has(key))
                continue
            seen.add(key)

            dists[i][j] += steps
            visitCounts[i][j] += 1

            q.push([i-1, j, steps+1])
            q.push([i+1, j, steps+1])
            q.push([i, j-1, steps+1])
            q.push([i, j+1, steps+1])
        }
    }
}