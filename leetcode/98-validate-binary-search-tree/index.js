/*
    1st approach: recursion
    - compare the node.val with min & max in each recursion
    
    Time 	O(N)
    Space	O(H)
    100 ms, faster than 30.58%
*/
var isValidBST = function (root) {
	return dfs(root, -Number.MAX_VALUE, Number.MAX_VALUE);
};

var dfs = function (node, min, max) {
	if (node === null) {
		return true;
	}
	if (node.val <= min || node.val >= max) {
		return false;
	}
	return dfs(node.left, min, node.val) && dfs(node.right, node.val, max);
};

/*
    2nd
*/
var isValidBST = function(root) {
    const check = (node, min, max) => {
        if (node == null) {
            return true
        }
        if (node.val <= min || node.val >= max) {
            return false
        }
        const left = check(node.left, min, node.val)
        const right = check(node.right, node.val, max)
        return left && right
    }
    return check(root, -(2**32)-1, 2**32)
};