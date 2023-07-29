/*
    backtracking

    LTE
    Time    O(2^N * 2^N * logA)
    Space   O(N)
*/
var maxScore = function(A) {
    const n = A.length
    const chosen = Array(n).fill(0)

    const dfs = steps => {
        let maxSum = 0
        for (let i = 0; i < n; i++) {
            for (let j = i+1; j < n; j++) {
                if (chosen[i] == 0 && chosen[j] == 0) {
                    let score = steps * gcd(A[i], A[j])
                    
                    chosen[i] = 1
                    chosen[j] = 1

                    score += dfs(steps+1)
                    maxSum = Math.max(maxSum, score)

                    chosen[i] = 0
                    chosen[j] = 0
                }
            }
        }
        return maxSum
    }

    return dfs(1)
};

const gcd = (a, b) => {
    if (b == 0) {
        return a
    }
    return gcd(b, a%b)
}

/*
    backtracking + caching

    LTE
    Time    O(2^N * 2^N * logA)
    Space   O(N)
*/
var maxScore = function(A) {
    const n = A.length
    const chosen = Array(n).fill(0)
    const cache = {}

    const dfs = steps => {
        const key = chosen.join(',')
        if (key in cache) {
            return cache[key]
        }
        let maxSum = 0
        for (let i = 0; i < n; i++) {
            for (let j = i+1; j < n; j++) {
                if (chosen[i] == 0 && chosen[j] == 0) {
                    let score = steps * gcd(A[i], A[j])
                    
                    chosen[i] = 1
                    chosen[j] = 1

                    score += dfs(steps+1)
                    maxSum = Math.max(maxSum, score)

                    chosen[i] = 0
                    chosen[j] = 0
                }
            }
        }
        cache[key] = maxSum
        return maxSum
    }

    return dfs(1)
};