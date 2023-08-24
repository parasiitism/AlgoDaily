/*
    sliding window
    
    Time    O(N)
    Space   O(1)
*/
var checkArray = function(nums, k) {
    const n = nums.length
    let cur = 0
    for (let i = 0; i < n; i++) {
        if (cur > nums[i]) {
            return false
        }
        // decrement the current element if we can do an operation e.g. previous element > 0
        nums[i] -= cur
        // increment the current remain for later increment
        cur += nums[i]
        // decrement the left-end of the sliding window
        if (i-k+1 >= 0) {
            cur -= nums[i-k+1]
        }
    }
    return cur == 0
};