/*
    dynamic programming
    - the idea is try all possibilites, and the optimize the time by caching
    - WHAT we store?
        - (left, right) of a stick, meaning that if we see this stick again, we get the result from cache
    - one trick here: put 0 and n into the cuts array, 
        so that we can avoid the edge cases where we need to deal with the boundary

    Time    O(N^3): cache[(left, right)] takes O(N^2), in every resursion we loop over the cuts which takes O(N)
    Space   O(N^2)
*/
var minCost = function(n, _cuts) {
    const cuts = [..._cuts, 0, n]
    cuts.sort((a, b) => a - b)
    const cache = {}

    const dfs = (L, R) => {
        if (R - L == 1) {
            return 0
        }
        const key = `${L},${R}`
        if (key in cache) {
            return cache[key]
        }
        let subResult = 2**32
        for (let i = L+1; i < R; i++) {
            const cost_left = dfs(L, i)
            const cost_right = dfs(i, R)
            const cost = cuts[R] - cuts[L]
            subResult = Math.min(subResult, cost_left + cost_right + cost)
        }
        cache[key] = subResult
        return subResult
    }

    return dfs(0, cuts.length-1)
};