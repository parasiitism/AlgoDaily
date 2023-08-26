/*
    2nd: global index
*/
var str2tree = function(s) {
    let idx = 0

    const dfs = () => {
        if (idx == s.length) {
            return null
        }
        let numStr = ''
        while (idx < s.length && s[idx] != '(' && s[idx] != ')') {
            numStr += s[idx]
            idx += 1
        }
        const num = Number(numStr)
        const node = new TreeNode(num)
        if (idx < s.length && s[idx] == '(') {
            idx += 1
            node.left = dfs()
        }
        if (idx < s.length && s[idx] == '(') {
            idx += 1
            node.right = dfs()
        }
        if (idx < s.length && s[idx] == ')') {
            idx += 1
        }
        return node
    }

    return dfs()
};