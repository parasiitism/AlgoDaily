/*
    1st: recursion
    - similar to lc77(combinations)

    Time    O(nCk)
    Space   O(nCk)
    80 ms, faster than 32.73% 
*/
var combinationSum3 = function (k, n) {
	const res = []
    const nums = [1,2,3,4,5,6,7,8,9]
    const dfs = (cands, chosen, total) => {
        if (chosen.length == k) {
            if (total == n) {
                res.push(chosen)
            }
            return
        }
        if (total >= n) {
            return
        }
        for (let i = 0; i < cands.length; i++) {
            const _cands = cands.slice(i+1)
            const _chosen = [...chosen, cands[i]]
            const _total = total + cands[i]
            dfs(_cands, _chosen, _total)
        }
    }
    dfs(nums, [], 0)
    return res
};

/*
    2nd: recursion
    - similar to lc77(combinations)

    Time    O(nCk)
    Space   O(nCk)
    80 ms, faster than 32.73% 
*/
var combinationSum3 = function(k, n) {
    const res = []
    const dfs = (chosen, idx, remain) => {
        if (chosen.length == k) {
            if (remain == 0) {
                res.push(chosen)
            }
            return
        } else if (remain < 0) {
            return
        }
        for (let i = idx; i <= 9; i++) {
            const _chosen = [...chosen, i]
            dfs(_chosen, i+1, remain - i)
        }
    }
    dfs([], 1, n)
    return res
};
