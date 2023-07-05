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
    return validate(root, -(2**32)-1, 2**32)
};

const validate = (node, left_limit, right_limit) => {
    if (node === null) {
        return true
    }
    if (node.val <= left_limit || node.val >= right_limit) {
        return false
    }
    if (validate(node.left, left_limit, node.val) == false) {
        return false
    }
    if (validate(node.right, node.val, right_limit) == false) {
        return false
    }
    return true
}