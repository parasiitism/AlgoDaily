/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const hs = {}
    for (let x of nums) {
        if (x in hs) {
            return true
        }
        hs[x] = 1
    }
    return false
};

/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const hs = new Set()
    for (let x of nums) {
        if (hs.has(x)) {
            return true
        }
        hs.add(x)
    }
    return false
};