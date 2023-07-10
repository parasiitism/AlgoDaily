/*
    Recursive DFS
    - the way similar to lc416
    - for each number, we can either include or exclude it the result, therefore we have 2^n options in total

    Time    O(2^n)
    Space   O(2^n) recursion tree
    92 ms, faster than 21.88% 
*/
var subsets = function (nums) {
	const res = []
    const dfs = (chosen, remain) => {
        res.push(chosen)
        for (let i = 0; i < remain.length; i++) {
            const _chosen = [...chosen, remain[i]]
            const _remain = remain.slice(i+1)
            dfs(_chosen, _remain)
        }
    }
    dfs([], nums)
    return res
};

/*
    Optimize 1st with indices only 
*/
var subsets = function(nums) {
    const res = []
    const dfs = (start, chosen) => {
        res.push(chosen)
        for (let i = start; i < nums.length; i++) {
            const c = nums[i]
            const _chosen = [...chosen, c]
            dfs(i+1, _chosen)
        }
    }
    dfs(0, [])

    return res
};