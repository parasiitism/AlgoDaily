/*
    1st: recursive dfs

    e.g. [1,2,3]
    1          2         3
    2,3 3,2   1,3  3,1    1,2 2,1

    - select k from n number, it is a permutation problem therefore, 
        the time complexity is nPk = n!/(n-k)!

    - the crux is dfs(nums[:i]+arr[i+1:], prefix+[nums[i]])
    
    84 ms, faster than 85.31%
*/
var permute = function (nums) {
	const res = []
    const dfs = (cands, chosen) => {
        if (cands.length == 0) {
            res.push(chosen)
        }
        for (let i = 0; i < cands.length; i++) {
            const _cands = [...cands.slice(0, i), ...cands.slice(i+1)]
            const _chosen = [...chosen, cands[i]]
            dfs(_cands, _chosen)
        }
    }
    dfs(nums, [])
    return res
};

/*
    2nd: backtracking

    Time    O(N * N!)
    Space   O(N)
*/
var permute = function(nums) {
    const res = []
    const backtrack = path => {
        if (path.length === nums.length) {
            res.push([...path])
        }
        for (let x of nums) {
            if (path.indexOf(x) === -1) {
                path.push(x)
                backtrack(path)
                path.pop()
            }
        }
    }
    backtrack([])
    return res
};