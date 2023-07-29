/*
    1st: math

    Time    O(N)
    Space   O(N)
    112 ms, faster than 17.76%
*/
var smallestRangeI = function(nums, k) {
    let smallest = nums[0]
    let largest = nums[0]
    for (let i = 0; i < nums.length; i++) {
        smallest = Math.min(smallest, nums[i])
        largest = Math.max(largest, nums[i])
    }
    return Math.max(0, largest - smallest - 2*k)
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