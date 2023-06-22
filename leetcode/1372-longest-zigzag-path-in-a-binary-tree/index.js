/*
    1st: recursion
    - keep track of the zigzag path(left, right) along the way when we traverse the tree
    - update our global resuslt if necessary

    Time    O(N)
    Space   O(N+H)
    548 ms, faster than 24.62%
*/
var longestZigZag = function(root) {
    let res = 0

    const dfs = (node, dir, L) => {
        if (node === null) {
            return
        }
        res = Math.max(res, L)

        if (dir.length === 0 || dir === 'L') {
            dfs(node.left, 'L', 1)
        } else {
            dfs(node.left, 'L', L+1)
        }
        
        if (dir.length === 0 || dir === 'R') {
            dfs(node.right, 'R', 1)
        } else {
            dfs(node.right, 'R', L+1)
        }
    }
    dfs(root, '', 0)

    return res
};