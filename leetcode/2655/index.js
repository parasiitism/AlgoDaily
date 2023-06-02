/*
    1st: sort
    - merge intervals and then the result is the missing range from 0 to N

    Time    O(NlogN)
    Space   O(N)
*/

/**
 * @param {number} n
 * @param {number[][]} ranges
 * @return {number[][]}
 */
var findMaximalUncoveredRanges = function(n, ranges) {
    ranges.sort((a, b) => a[0] - b[0])
    let M = []
    for (let [s, e] of ranges) {
        if (M.length > 0 && s <= M[M.length-1][1]) {
            M[M.length-1][1] = Math.max(M[M.length-1][1], e)
        } else {
            M.push([s ,e])
        }
    }
    M = [[-1,-1], ...M, [n, n]] // put the asking range in, so easier to iterate
    const res = []
    for (let i = 1; i < M.length; i++) {
        const prev_end = M[i-1][1] + 1
        const cur_start = M[i][0] - 1
        
        if (prev_end <= cur_start) {
            res.push([prev_end, cur_start])
        }
    }
    return res
};