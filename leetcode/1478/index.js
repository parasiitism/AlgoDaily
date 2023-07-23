/*
    DP
    1. for every pair of (i, j), compute the median
    2. recursively try all medians to place the mailbox 1 by 1
    3. use a hashtable to avoid redundant calculation

    learned from others
    - https://leetcode.com/problems/allocate-mailboxes/solutions/685620/java-c-python-top-down-dp-prove-median-mailbox-o-n-3/

    Time    O(N^3 + NK)
    Space   O(N^2)
*/
var minDistance = function(houses, k) {
    const n = houses.length
    houses.sort((a, b) => a - b)
    
    const dists = []
    for (let i=0; i < n; i++) {
        dists.push(Array(n).fill(0))
    }

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            const midIdx = Math.floor((i + j)/2)
            const medianPos = houses[midIdx]
            for (let k = i; k <= j; k++) {
                dists[i][j] += Math.abs(medianPos - houses[k])
            }
        }
    }

    const cache = {}
    const dfs = (i, k) => {
        if (i == n && k == 0) {
            return 0
        }
        if (k == 0 || i == n) {
            return 2**32
        }
        const key = `${i},${k}`
        if (key in cache) {
            return cache[key]
        }
        let minDist = 2**32
        for (let j = i; j < n; j++) {
            const d = dists[i][j]
            minDist = Math.min(minDist, d + dfs(j+1, k-1))
        }
        cache[key] = minDist
        return minDist
    }

    return dfs(0, k)
};