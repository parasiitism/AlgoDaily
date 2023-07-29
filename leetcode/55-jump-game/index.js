var canJump = function(nums) {
    let maxIdx = 0
    for (let i = 0; i < nums.length; i++) {
        if (i > maxIdx) {
            return false
        }
        maxIdx = Math.max(maxIdx, i + nums[i])
    }
    return true
};
