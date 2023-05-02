/*
    Given a tree indicating a sewer drainage system for n nodes, your task is to divide the system
    into 2 smaller pieces by cutting one branch so that the total flows of the resulting subtrees are as close as possible.

    e.g.1
    Input:
    parent = [-1, 0, 0, 1, 1, 2],
    values = [1,  2, 2, 1, 1, 1]

    Output:
    0

    e.g.2
    Input:
    [-1, 0, 1, 2],
    [1, 4, 3, 4]
    
    Output:
    2

    e.g.3
    Input:
    [-1, 0, 0, 0],
    [10, 11, 10, 10]
    
    Output:
    19
*/
var f = function(parent, input) {
    const n = parent.length
    const G = {}
    for (let i = 0; i < n; i++) {
        G[i] = []
    }
    for (let i = 0; i < n; i++) {
        const p = parent[i]
        if (p > -1) {
            G[p].push(i)
        }
    }

    const candidates = []
    
    const dfs = node => {
        let subTreeSum = input[node]
        for (let child of G[node]) {
            subTreeSum += dfs(child)
        }
        candidates.push(subTreeSum)
        return subTreeSum
    }

    let res = 2**32
    const total = dfs(0)
    for (let cand of candidates) {
        const diff = Math.abs(total - cand - cand)
        res = Math.min(res, diff)
    }

    return res
}

console.log(f(
    [-1, 0, 0, 1, 1, 2],
    [1,  2, 2, 1, 1, 1]
))

console.log(f(
    [-1, 0, 1, 2],
    [1, 4, 3, 4]
))

console.log(f(
    [-1, 0, 0, 0],
    [10, 11, 10, 10]
))