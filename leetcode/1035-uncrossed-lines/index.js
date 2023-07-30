/*
    3rd: similar as 2nd, but more concise
    - recursion + hashtable, bottom up
    - recursion to generate all possibilities
    - use a hashtable to cache the max number of feasible crosses from the end to avoid redundant calculations

    Time    O(N^2)
    Space   O(N^2)
    616 ms, faster than 6.46%
*/
var maxUncrossedLines = function(A, B) {
    const cache = {}
    const dfs = (i, j) => {
        if (i == A.length || j == B.length) {
            return 0
        }
        const key = `${i},${j}`
        if (key in cache) {
            return cache[key]
        }
        let total = 0
        if (A[i] == B[j]) {
            total = Math.max(total, dfs(i+1, j+1) + 1)
        }
        total = Math.max(total, dfs(i+1, j))
        total = Math.max(total, dfs(i, j+1))
        cache[key] = total
        return total
    }
    return dfs(0, 0)
};