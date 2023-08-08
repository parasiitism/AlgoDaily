/*
    1st: recursion, backtracking

    Time    O(N * 2^R) R: requests
    Space   O(N + R)
*/

/**
 * @param {number} n
 * @param {number[][]} requests
 * @return {number}
 */
var maximumRequests = function(n, requests) {
    const building_cap = Array(n).fill(0)
    let res = 0

    const backtrack = (index, count) => {
        if (index === requests.length) {
            for (let i = 0; i < n; i++) {
                if (building_cap[i] !== 0) {
                    return
                }
            }
            res = Math.max(res, count)
            return
        }
        // consider
        const [from, to] = requests[index]
        building_cap[from] -= 1
        building_cap[to] += 1
        backtrack(index+1, count+1)
        building_cap[from] += 1
        building_cap[to] -= 1
        
        // not consider
        backtrack(index+1, count)
    }

    backtrack(0, 0)

    return res
};