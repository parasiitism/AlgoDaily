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
        let max_lines = 0
        if (A[i] === B[j]) {
            max_lines = dfs(i+1, j+1) + 1
        } else {
            const a = dfs(i+1, j)
            const b = dfs(i, j+1)
            max_lines = Math.max(a, b)
        }
        cache[key] = max_lines
        return max_lines
    }

    return dfs(0, 0)
};