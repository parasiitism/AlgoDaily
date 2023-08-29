/*
    Dynamic Programming
    - combination sum

    Time    O(NX)
    Space   O(NX)
*/
var numberOfWays = function(n, x) {
    const MOD = 10**9+7
    const cache = {}

    const dfs = (i, remain) => {
        if (remain == 0) {
            return 1
        }
        if (remain < 0 || i**x > remain) {
            return 0
        }
        const key = `${i},${remain}`
        if (key in cache) {
            return cache[key]
        }
        let total = 0
        total += dfs(i+1, remain)
        total += dfs(i+1, remain - i**x)
        cache[key] = total % MOD
        return cache[key]
    }
    return dfs(1, n)
};