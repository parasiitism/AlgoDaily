/*
    1st: dynamic programming

    Time    O(1000N)
    Space   O(N)
*/
var jump = function(nums) {
    const n = nums.length
    const cache = {}
    const dfs = i => {
        if (i >= n-1) {
            return 0
        }
        if (i in cache) {
            return cache[i]
        }
        const x = nums[i]
        if (x == 0) {
            return 2**32
        }
        let minSteps = 2**32
        for (let j=1; j<=x; j++) {
            const temp = dfs(i+j) + 1
            minSteps = Math.min(minSteps, temp)
        }
        cache[i] = minSteps
        return minSteps
    }

    const res = dfs(0)
    return res
};

/*
    4th: greedy
    - similar to lc55: Jump Game I
    - here we have 2 more variables
        - jumps: track the number of jumps
        - gMaxIdx: track the global farthest index we can reach
    
    Time    O(N)
    Space   O(1)
*/
var jump = function(nums) {
    let resMaxIdx = 0
    let curMaxIdx = 0
    let jumps = 0
    for (let i = 0; i < nums.length-1; i++) {
        resMaxIdx = Math.max(resMaxIdx, i+nums[i])
        if (i == curMaxIdx) {
            jumps += 1
            curMaxIdx = resMaxIdx
        }
    }
    return jumps
};
/*
    OR
*/
var jump = function(nums) {
    let resMaxIdx = 0
    let curMaxIdx = 0
    let jumps = 0
    for (let i = 0; i < nums.length; i++) {
        if (i > resMaxIdx) {
            jumps += 1
            resMaxIdx = curMaxIdx
        }
        curMaxIdx = Math.max(curMaxIdx, i+nums[i])
    }
    return jumps
};