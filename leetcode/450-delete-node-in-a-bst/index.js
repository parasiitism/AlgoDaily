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
var deleteNode = function(root, key) {
    if (root === null) {
        return null
    }
    if (key < root.val) {
        root.left = deleteNode(root.left, key)
    } else if (key > root.val) {
        root.right = deleteNode(root.right, key)
    } else {
        if (root.left === null && root.right === null) {
            return null
        } else if (root.left === null) {
            return root.right
        } else if (root.right === null) {
            return root.left
        } else {
            const successor = leftMostFromRight(root.right)
            root.val = successor.val
            root.right = deleteNode(root.right, successor.val)
            return root
        }
    }
    return root
};

const leftMostFromRight = root => {
    let cur = root
    while (cur.left !== null) {
        cur = cur.left
    }
    return cur
}