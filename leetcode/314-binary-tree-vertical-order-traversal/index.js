/*
    2nd approach: bfs + hashtable
    - similar to lc987

    Time    O(N)
    Space   O(N)
    88 ms, faster than 67.26%
*/
var verticalOrder = function(root) {
    if (root === null) {
        return []
    }
    const q = [[root, 0]]
    const cache = {} // key: [node.val,...]
    let minCol = 0
    let maxCol = 0
    while (q.length > 0) {
        const [node, vIdx] = q.shift()
        minCol = Math.min(minCol, vIdx)
        maxCol = Math.max(maxCol, vIdx)
        if (vIdx in cache === false) {
            cache[vIdx] = []
        }
        cache[vIdx].push(node.val)
        if (node.left !== null) {
            q.push([node.left, vIdx - 1])
        }
        if (node.right !== null) {
            q.push([node.right, vIdx + 1])
        }
    }
    const res = []
    for (let i = minCol; i <= maxCol; i++) {
        const values = cache[i]
        res.push(values)
    }
    return res
};
