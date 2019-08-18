/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
    let cur = Number.MIN_SAFE_INTEGER
    let res = Number.MIN_SAFE_INTEGER
    for (let x of nums) {
        cur = Math.max(cur + x, x)
        res = Math.max(res, cur)
    }
    return res
};