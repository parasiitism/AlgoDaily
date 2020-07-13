/*
    1st approach: recursion

	Time	O(n)
	Space	O(h)
	0 ms, faster than 100.00%
*/
var isSameTree = function (p, q) {
	if (p == null && q == null) {
		return true;
	} else if (p == null || q == null) {
		return false;
	}
	return (
		p.val == q.val &&
		isSameTree(p.left, q.left) &&
		isSameTree(p.right, q.right)
	);
};

/*
    2nd approach: dfs using a stack

	Time	O(n)
	Space	O(h)
	0 ms, faster than 100.00%
*/
var isSameTree = function (p, q) {
	const stack = [[p, q]];
	while (stack.length > 0) {
		const [a, b] = stack.pop();

		if (a == null && b == null) {
			continue;
		} else if (a == null || b == null || a.val !== b.val) {
			return false;
		}
		stack.push([a.left, b.left]);
		stack.push([a.right, b.right]);
	}
	return true;
};
