/*
    Time    O(N)
    Space   O(1)
*/
var sumOfSquares = function(nums) {
    const n = nums.length
    let res = 0
    for (let i = 0; i < n; i++) {
        if (n % (i+1) == 0) {
            res += nums[i]**2
        }
    }
    return res
};