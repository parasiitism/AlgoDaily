var binaryTreePaths = function(root) {
    const paths = []
    const dfs = (node, path) => {
        if (node === null) { return }
        const newPath = [...path, node.val]
        if (node.left === null && node.right === null) {
            paths.push([...newPath])
        }
        dfs(node.left, [...newPath])
        dfs(node.right, [...newPath])
    }
    dfs(root, [])
    return paths.map(p => p.join("->")
};