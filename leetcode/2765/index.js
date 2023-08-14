/**
 * @param {number[]} nums
 * @return {number}
 */
var alternatingSubarray = function(A) {
    const n = A.length
    let res = 0
    for (let i = 0; i < n-1; i++) {
        let j = i+1
        let diff = A[j] - A[i]
        if (A[j] - A[i] !== 1) {
            continue
        }
        while (j+1 < n && A[j+1] - A[j] == -diff) {
            diff = A[j+1] - A[j]
            j += 1
        }
        res = Math.max(res, j - i + 1)
    }  
    return res > 1 ? res : -1
};