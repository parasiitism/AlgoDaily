var subtreeWithAllDeepest = function(root) {
    const dfs = node => {
        if (node === null) {
            return [0, null]
        }
        const [left_depth, left_res] = dfs(node.left)
        const [right_depth, right_res] = dfs(node.right)
        if (left_depth < right_depth) {
            return [right_depth+1, right_res]
        } else if (left_depth > right_depth) {
            return [left_depth+1, left_res]
        }
        return [left_depth+1, node]
    }
    return dfs(root)[1]
};