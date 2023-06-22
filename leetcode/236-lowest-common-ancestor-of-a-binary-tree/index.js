/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/*
    2nd: recursion

    Time    O(N)
    Space   O(N)
    88 ms, faster than 91.45%
*/
var lowestCommonAncestor = function (root, p, q) {
	if (root === null || root.val == p.val || root.val == q.val) {
        return root
    }
    const L = lowestCommonAncestor(root.left, p, q)
    const R = lowestCommonAncestor(root.right, p, q)
    if (L !== null && R !== null) {
        return root
    } else if (L !== null) {
        return L
    } else if (R !== null) {
        return R
    }
    return null
};
