/*
    2nd: dynamic programming - recursion + hashtable
    1. for each distinct number, accumulate the sum
        e.g. [2, 2, 3, 3, 3, 5, 7, 8, 8]
        -> [ (2, 4), (3,9), (5, 5), (7, 7), (8, 16)] <- (distinct number, sum)
    2. sort them
    3. do lc198: house robber

    Time    O(NlogN)
    Space   O(N)
    111 ms, faster than 10.34%
*/
var deleteAndEarn = function(nums) {
    const ht = {}
    for (let x of nums) {
        if (x in ht === false) {
            ht[x] = 0
        }
        ht[x] += x
    }
    const kvs = Object.entries(ht)
    kvs.sort((a, b) => a[0] - b[0])

    const cache = {}
    const dfs = i => {
        if (i >= kvs.length) {
            return 0
        }
        if (i in cache) {
            return cache[i]
        }
        if (i+1 < kvs.length && kvs[i][0] == kvs[i+1][0] - 1) {
            const a = dfs(i+1)
            const b = dfs(i+2) + kvs[i][1]
            const best = Math.max(a, b)
            cache[i] = best
            return best
        }
        const c = dfs(i+1) + kvs[i][1]
        cache[i] = c
        return c
    }
    return dfs(0)
};