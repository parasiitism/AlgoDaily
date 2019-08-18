/**
 * @param {number[]} nums
 * @return {number}
 * 
 * 
 * 1st approach: hashtable

    Time    O(2n)
    Space   O(n)
    60 ms, faster than 80.96%
 */
var majorityElement = function (nums) {
    const m = {}
    for (let i = 0; i < nums.length; i++) {
        let x = nums[i]
        if (m[x] == undefined) {
            m[x] = 1
        } else {
            m[x] += 1
        }
        if (m[x] > Math.floor(nums.length / 2)) {
            return x
        }
    }
};