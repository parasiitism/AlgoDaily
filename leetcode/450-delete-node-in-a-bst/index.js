/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} key
 * @return {TreeNode}
 */
var deleteNode = function(node, key) {
    if (node == null) {
        return null
    }
    if (key < node.val) {
        node.left = deleteNode(node.left, key)
    } else if (key > node.val) {
        node.right = deleteNode(node.right, key)
    } else {
        if (!node.left && !node.right) {
            return null
        } else if (!node.left) {
            return node.right
        } else if (!node.right) {
            return node.left
        } else {
            const succ = getMinFromRight(node.right)
            succ.left = node.left
            return node.right
        }
    }
    return node
};

const getMinFromRight = node => {
    let cur = node
    while (cur.left != null) {
        cur = cur.left
    }
    return cur
}