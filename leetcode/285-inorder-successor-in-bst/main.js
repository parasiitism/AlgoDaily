/**
 * Definition for a binary tree node.
 */
function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @return {TreeNode}
 */

// OMG, how can people come up with this solution, not intuitive at the first glance

var inorderSuccessor = function(root, p) {
  let successor = null;
  let node = root;
  while (node !== null) {
    if (p.val < node.val) {
        successor = node;
        node = node.left;
    } else {
        node = node.right;
    }
  }
  return successor;
};

let a = new TreeNode(2)
let b = new TreeNode(1)

ans = inorderSuccessor(a, b)
console.log(ans)