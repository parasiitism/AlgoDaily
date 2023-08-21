/*
    DP
    - straightforward, for every index, 
        just iterate thru the left hand side and see which can be the base to jump

    Time    O(N^2)
    Space   O(N)
    143ms beats 68.28%
*/
var maximumJumps = function(nums, target) {
    const n = nums.length
    const dp = Array(n).fill(0)
    for (let i = 0; i < n; i++) {
        let maxSteps = 0
        for (let j = 0; j < i; j++) {
            // catch: remember to skip the stones that we never jumped to
            if (j != 0 && dp[j] == 0) {
                continue
            }

            if (Math.abs(nums[j] - nums[i]) <= target) {
                maxSteps = Math.max(maxSteps, dp[j] + 1)
            }
        }
        dp[i] = maxSteps
    }
    if (dp[dp.length-1] == 0) {
        return -1
    }
    return dp[dp.length-1]
};