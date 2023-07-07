/*
    2nd: BFS + hashtable to avoid redundant revisit

    e.g. a/b = 2, b/c = 3
    means
    a -> b = 2
    b -> c = 3
    so, a -> b -> c = 2 * 3 = 6
    therefore, 
    we can start BFS from 1.0,
    after BFS, ratio = 1.0 * graph[a][b] * graph[b][c] = 1 * 2 * 3 = 6

    Time    O(N + QN) Q: number of queries, N: number of equations
    Space   O(Q+N)
    76 ms, faster than 75.12%
*/
var calcEquation = function(equations, values, queries) {
    const n = equations.length
    const G = {}
    for (let i = 0; i < n; i++) {
        const [u, v] = equations[i]
        const ratio = values[i]
        if (u in G === false) { G[u] = {} }
        if (v in G === false) { G[v] = {} }
        G[u][v] = ratio
        G[v][u] = 1.0 / ratio
    }
    const res = []
    for (let [a ,b] of queries) {
        const ratio = bfs(G, a, b)
        res.push(ratio)
    }
    return res
};

const bfs = (G, src, dest) => {
    if (src in G === false || dest in G === false) {
        return -1
    }
    const q = [[src, 1.0]]
    const seen = new Set()
    while (q.length > 0) {
        const [node, ratio] = q.shift()
        if (node === dest) {
            return ratio
        }
        if (seen.has(node)) {
            continue
        }
        seen.add(node)
        for (key in G[node]) {
            const to_multiply = G[node][key]
            q.push([key, ratio * to_multiply])
        }
    }
    return -1.0
}

/*
    followup: real time

    see ~/glassdoor/bloomberg/currency-exchange
*/