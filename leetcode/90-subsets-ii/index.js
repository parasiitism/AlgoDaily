/*
    2nd approach: recursion
    - similar to 1st dont need to use a hashtable(since the array is sorted)
    
    Time    O(2^n) worst
    Space   O(2^n) recursion
    88 ms, faster than 54.52%
*/
var subsetsWithDup = function (nums) {
	nums.sort((a, b) => a - b);
	const res = [];
	const dfs = (cands, chosen) => {
		res.push(chosen);
		for (let i = 0; i < cands.length; i++) {
            if (i-1 >= 0 && cands[i-1] == cands[i]) {
                continue
            }
            const _cands = cands.slice(i+1)
            const _chosen = [...chosen, cands[i]]
            dfs(_cands, _chosen)
		}
	};
	dfs(nums, []);
	return res;
};

/*
    Optimize 1st with indices only 
*/
var subsetsWithDup = function(nums) {
    nums.sort((a, b) => a - b)
    const res = []
    const dfs = (start, chosen) => {
        res.push(chosen)
        for (let i = start; i < nums.length; i++) {
            if (i-1 >= start && nums[i-1] === nums[i]) {
                continue
            }
            const c = nums[i]
            const _chosen = [...chosen, c]
            dfs(i+1, _chosen)
        }
    }
    dfs(0, [])

    return res
};