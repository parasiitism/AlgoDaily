/*
    1st: BFS

    Time    O(RC) but pop(0) takes O(N) so it should be slow
    Space   O(RC)
    856 ms, faster than 33.33%
*/
var nearestExit = function(maze, entrance) {
    const R = maze.length
    const C = maze[0].length
    const [x, y] = entrance
    const q = [[x, y, 0, null]]
    const seen = new Set()
    while (q.length > 0) {
        const [i, j, steps, prev] = q.shift()
        if (i < 0 || i === R || j < 0 || j === C) {
            if (prev != `${x},${y}`) {
                return steps - 1
            }
            continue
        }
        if (maze[i][j] === '+') {
            continue
        }
        const key = `${i},${j}`
        if (seen.has(key)) {
            continue
        }
        seen.add(key)

        q.push([i-1, j, steps+1, key])
        q.push([i+1, j, steps+1, key])
        q.push([i, j-1, steps+1, key])
        q.push([i, j+1, steps+1, key])
    }
    return -1
};