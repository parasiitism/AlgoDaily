/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
    const m = {}
    for (let i = 0; i < nums.length; i++) {
        const remain = target - nums[i]
        if (m[remain] != undefined) {
            return [m[remain], i]
        }
        m[nums[i]] = i
    }
    return [-1, -1]
};