/*
    1st: prefix sum

    Time    O(N)
    Space   O(1)
    36 ms, faster than 100.00%
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function(nums) {
    let pfs = 0
    let dip = 2**32
    for (let x of nums) {
        pfs += x
        dip = Math.min(dip, pfs)
    }
    if (dip < 1) {
        return 1 - dip
    }
    return 1
};