/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 * 
 * 1st: binary search
 * 
 * Time     O(2logn)
 * Space    O(1)
 * 44ms beats 95.59%
 */
var isMajorityElement = function (nums, target) {
    const left = bsearchLower(nums, target)
    const right = bsearchUpper(nums, target)
    if (nums[left] != target) {
        return false
    }
    const count = right - left
    return count > Math.floor(nums.length / 2)
};

var bsearchLower = function (nums, target) {
    let left = 0
    let right = nums.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target <= nums[mid]) {
            right = mid
        } else {
            left = mid + 1
        }
    }
    return left
}

var bsearchUpper = function (nums, target) {
    let left = 0
    let right = nums.length
    while (left < right) {
        const mid = Math.floor((left + right) / 2)
        if (target >= nums[mid]) {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 * 
 * 2nd: brute force
 * 
 * Time     O(n)
 * Space    O(1)
 * 56 ms, faster than 47.06%
 */
var isMajorityElement = function (nums, target) {
    let count = 0
    for (let i = 0; i < nums.length; i++) {
        let x = nums[i]
        if (x === target) {
            count++
        }
    }
    return count > Math.floor(nums.length / 2)
};