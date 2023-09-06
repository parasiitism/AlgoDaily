class UnionFind {
    constructor(n) {
        this.n = n
        this.parents = {}
        this.caps = {}
        for (let i = 0; i < n; i++) {
            this.parents[i] = i
            this.caps[i] = 1
        }
    }
    find(node) {
        if (node in this.parents === false) { return -1 }
        let cur = node
        while (cur != this.parents[cur]) {
            cur = this.parents[cur]
        }
        return cur
    }
    union(u, v) {
        const rootU = this.find(u)
        const rootV = this.find(v)
        if (rootU == -1 || rootV == -1 || rootU == rootV ) { return }
        if (this.caps[rootU] < this.caps[rootV]) {
            this.parents[rootU] = rootV
            this.caps[rootV] += this.caps[rootU]
        } else {
            this.parents[rootV] = rootU
            this.caps[rootU] += this.caps[rootV]
        }
        this.n -= 1
    }
}

var makeConnected = function(n, connections) {
    if (connections.length < n-1 ) {
        return -1
    }
    const uf = new UnionFind(n)
    for (let [u, v] of connections) {
        uf.union(u, v)
    }
    return uf.n - 1
};