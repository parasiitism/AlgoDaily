var getAncestors = function(n, edges) {
    const parents = {} // child = parents[]
    const cache = {}
    for (let i = 0; i < n; i++) {
        parents[i] = []
        cache[i] = new Set()
    }
    for (let [from, to] of edges) {
        parents[to].push(from)
    }
    for (let i = 0; i < n; i++) {
        const q = [i]
        while (q.length > 0) {
            const node = q.shift()
            if (cache[i].has(node)) {
                continue
            }
            cache[i].add(node)
            for (let p of parents[node]) {
                q.push(p)
            }
        }
    }
    const res = []
    for (let i = 0; i < n; i++) {
        cache[i].delete(i)
        const ancestors = Array.from(cache[i])
        ancestors.sort((a, b) => a - b)
        res.push(ancestors)
    }
    return res
};