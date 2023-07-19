/*
    brute-force DFS
    - first, for every node, count how many times it would be visited for every trip
    - and then DFS from any node(e.g. start from node 0) to get the min cost

    Time    O(VT + V^2) T: trips, V: vertices
    Space   O(V*2)
*/

var minimumTotalPrice = function(n, edges, price, trips) {
    // build graph
    const G = {}
    for (let i = 0; i < n; i++) {
        G[i] = []
    }
    for (let [u, v] of edges) {
        G[u].push(v)
        G[v].push(u)
    }
    // count visisted
    const count = Array(n).fill(0)
    const countVisits = (node, parent, end) => {
        if (node === end) {
            count[node] += 1
            return true
        }
        for (let nb of G[node]) {
            if (nb != parent && countVisits(nb, node, end)) {
                count[node] += 1
                return true
            }
        }
        return false
    }
    for (let [s, e] of trips) {
        countVisits(s, null, e)
    }
    // 
    const getMinCost = (node, parent) => {
        let original = price[node] * count[node]
        let halved = price[node] * count[node] / 2
        for (let nb of G[node]) {
            if (nb != parent) {
                const [o, h] = getMinCost(nb, node)
                original += Math.min(o, h)
                halved += o
            }
        }
        return [original, halved]
    }
    // 
    const [original, halved] = getMinCost(0, null)
    return Math.min(original, halved)
};