/*
    2nd approach: recursive dfs, avoid duplicate by considering the candidates which are >= num
    - we need to show all combinations instead of just the count, so we need to reverse all branches in the recursion tree

    Time    O(N^k) k depends on target
    Space   O(N^N)
    104 ms, faster than 50.08% 
*/
var combinationSum = function(candidates, target) {
    candidates.sort((a, b) => a - b)

    const res = []
    const dfs = (chosen, remain) => {
        if (remain < 0) {
            return
        }
        if (remain == 0) {
            return res.push(chosen)
        }
        for (let i = 0; i < candidates.length; i++) {
            const c = candidates[i]
            if (chosen.length === 0 || chosen[chosen.length-1] <= c) {
                const _chosen = [...chosen, c]
                const _target = remain - c
                dfs(_chosen, _target)
            }
        }
    }
    dfs([], target)

    return res
};
