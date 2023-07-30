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
    const keySum = {}
    for (let x of nums) {
        if (x in keySum === false) {
            keySum[x] = 0
        }
        keySum[x] += x
    }
    const kvs = Object.entries(keySum)
    kvs.sort((a, b) => a[0] - b[0])

    const cache = {}
    const dfs = idx => {
        if (idx >= kvs.length) {
            return 0
        }
        if (idx in cache) {
            return cache[idx]
        }
        let total = 0
        if (idx+1 < kvs.length && Number(kvs[idx][0])+1 == Number(kvs[idx+1][0])) {
            const a = dfs(idx+1)
            const b = dfs(idx+2) + kvs[idx][1]
            total = Math.max(a, b)
        } else {
            total = dfs(idx+1) + kvs[idx][1]
        }   
        cache[idx] = total
        return total
    }
    return dfs(0)
};