/*
    1st: math

    Time    O(N)
    Space   O(N)
    112 ms, faster than 17.76%
*/
var smallestRangeI = function(nums, k) {
    let min = 2**32
    let max = -(2**32)
    for (let x of nums) {
        min = Math.min(min, x)
        max = Math.max(max, x)
    }
    return Math.max(max-k - (min+k), 0)
};
/*
    2nd: sort + compare the min and max
*/
var smallestRangeI = function(nums, k) {
    if (nums.length <= 1) {
        return 0
    } 
    nums.sort((a, b) => a - b)
    return Math.max(nums[nums.length-1] - k - (nums[0] + k), 0)
};