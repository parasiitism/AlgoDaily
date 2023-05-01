/*
    2nd approach: bfs
    - get the friend list for each friend
    - for each person, bfs to find all of his friends and put them into history
    - after finished one bfs, it means that we are done with one 'cluster'

    Time		O(NN) N: number of people
    Space		O(N)
    92 ms, faster than 46.85%
*/
var findCircleNum = function(isConnected) {
    const n = isConnected.length
    let res = 0
    const seen = new Set()
    for (let i = 0; i < n; i++) {
        if (seen.has(i)) {
            continue
        }
        bfs(isConnected, i, seen)
        res += 1
    }
    return res
};

const bfs = (isConnected, start, seen) => {
    const q = [start]
    while (q.length > 0) {
        const i = q.shift()
        if (seen.has(i)) {
            continue
        }
        seen.add(i)
        for (let j = 0; j < isConnected[i].length; j++) {
            if (isConnected[i][j] == 1) {
                q.push(j)
            }
        }
    }
}