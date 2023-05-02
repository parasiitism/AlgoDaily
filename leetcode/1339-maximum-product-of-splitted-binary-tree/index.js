/*
    1st: recursion
    1. first calculate the sum of all nodes' value
    2. for every subtree, calculate the product by using subtreeSum * (total-subtreeSum), update the global result if necessary

    Time    O(2N)
    Space   O(N)
    149 ms, faster than 73.21%
*/

var maxProduct = function(root) {
    const MOD = (10**9)+7
    const candidates = []
    
    const dfs = node => {
        if (node == null) {
            return 0
        }
        const left = dfs(node.left)
        const right = dfs(node.right)
        const subTreeSum = node.val + left + right
        candidates.push(subTreeSum)
        return subTreeSum 
    }

    let res = 0
    const total = dfs(root)
    for (let cand of candidates) {
        const x = cand * (total - cand)
        res = Math.max(res, x)
    }

    return res % MOD
};