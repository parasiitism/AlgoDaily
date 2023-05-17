/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var rowAndMaximumOnes = function(mat) {
    let max_sum_idx = -1
    let max_sum = -1
    for (let i = 0; i < mat.length; i++) {
        const sum = mat[i].reduce((acc, cur) => acc+cur, 0)
        if (sum > max_sum) {
            max_sum = sum
            max_sum_idx = i
        }
    }
    return [max_sum_idx, max_sum]
};