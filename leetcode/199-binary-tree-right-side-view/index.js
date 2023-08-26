/*
    1st approach: bfs
    - declare a result array
    - when we traverse down, put the val into the result if the depth >= len(array)

    Time    O(n)
    Space   O(h)
    104 ms, faster than 17.31%
*/
var rightSideView = function (root) {
	if (root === null) {
        return []
    }
    const q = [root]
    let res = []
    while (q.length > 0) {
        const n = q.length
        for (let i = 0; i < n; i++) {
            const node = q.shift()
            if (i === 0) {
                res.push(node.val)
            }
            if (node.right) {
                q.push(node.right)
            }
            if (node.left) {
                q.push(node.left)
            }
        }
    }
    return res
};

/*
    2nd approach: dfs
    - declare a result array
    - when we traverse down, put the val into the result if the depth >= len(array)

    Time    O(n)
    Space   O(h)
    80 ms, faster than 81.25%
*/
var rightSideView = function(root) {
    const res = []
    const dfs = (node, level) => {
        if (node == null) {
            return
        }
        if (level >= res.length) {
            res.push(node.val)
        }
        dfs(node.right, level+1)
        dfs(node.left, level+1)
    }
    dfs(root, 0)
    return res
};