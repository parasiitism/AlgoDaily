/*
    1st: dp
    - similar to lc518, the only difference is
    - lc518 doesn't care about the order
    - this question cares
    
    Time    O(NA)
    Space   O(N)
    92 ms, faster than 35.05%
*/
var combinationSum4 = function (nums, target) {
	if (target == 0) {
		return 1;
	}
	const ways = Array(target + 1).fill(0);
	ways[0] = 1;
	for (let j = 1; j <= target; j++) {
		for (let c of nums) {
			const remain = j - c;
			if (remain >= 0) {
				ways[j] += ways[remain];
			}
		}
	}
	return ways[target];
};

/*
    2nd: recursion + hashtable
    - similar to lc1155
    - unlike coin change 1 & 2, here we need to find out all the combinations, 
    so it is eaiser to use the roll dice approach

    Time    O(NA)
    Space   O(N)
    84 ms, faster than 64.90%
*/
var combinationSum4 = function(nums, target) {
    const cache = {}
    const dfs = remain => {
        if (remain < 0) {
            return 0
        }
        if (remain == 0) {
            return 1
        }
        if (remain in cache) {
            return cache[remain]
        }
        let total = 0
        for (let i = 0; i < nums.length; i++) {
            const x = nums[i]
            total += dfs(remain - x)
        }
        cache[remain] = total
        return total
    }
    return dfs(target)
};
