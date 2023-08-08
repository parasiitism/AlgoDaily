/*
    1st: brute-force
    - check every subarray

    Time    O(N^2)
    Space   O(1)
*/


/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
var longestAlternatingSubarray = function(A, threshold) {
    const n = A.length
    let res = 0
    for (let i = 0; i < n; i++) {
        if (A[i] % 2 === 1 || A[i] > threshold) {
            continue
        }
        let length = 1
        for (let j = i+1; j < n; j++) {
            if (A[j-1] % 2 === A[j] % 2 || A[j] > threshold) {
                break
            }
            length += 1
        }
        res = Math.max(res, length)
    }
    return res
};

/*
    2nd: 2 pointers
*/
var longestAlternatingSubarray = function(A, threshold) {
    const n = A.length
    let res = 0
    let i = 0
    while (i < n) {
        if (A[i] % 2 === 1 || A[i] > threshold) {
            i += 1
        } else {
            let j = i
            while (j+1 < n && A[j] % 2 !== A[j+1] % 2 && A[j+1] <= threshold) {
                j += 1
            }
            res = Math.max(res, j - i + 1)
            i = j+1
        }
    }
    return res
};