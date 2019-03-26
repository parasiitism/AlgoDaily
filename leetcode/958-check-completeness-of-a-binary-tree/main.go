package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach:
	1. dfs to count the depth for each leafs
	2. compare the depths and check if there are increasing or depths+1<maxdepth

	e.g.1
				1
			2		3
		4 5	 6
	the depths are [3,3,3,2], which is a complets tree

	e.g.2
				1
			2		3
		4 5	 	 6
	the depths are [3,3,2,3], which is not a complets tree

	Time	O(2n)
	Space	O(h)
	0 ms, faster than 100.00%
*/
func isCompleteTree(root *TreeNode) bool {
	if root == nil {
		return true
	}
	arr := []int{}
	var dfs func(node *TreeNode, cnt int)
	dfs = func(node *TreeNode, cnt int) {
		if node.Left == nil && node.Right == nil {
			arr = append(arr, cnt)
		} else if node.Left == nil {
			arr = append(arr, cnt)
			dfs(node.Right, cnt+1)
		} else if node.Right == nil {
			dfs(node.Left, cnt+1)
			arr = append(arr, cnt)
		} else {
			dfs(node.Left, cnt+1)
			dfs(node.Right, cnt+1)
		}
	}
	dfs(root, 1)

	depth := arr[0]
	prev := arr[0]
	for i := 1; i < len(arr); i++ {
		num := arr[i]
		/*
			check depths difference
			- no increasing
			- no larger than the depth from left
			- no different more than 1
		*/
		if num > depth || num > prev || num+1 < depth {
			return false
		}
		prev = num
	}
	return true
}

/*
	2nd approach:
	1. bfs and the queue finally should have all the leafs including null
	2. for a complete binary tree, there should not be any node after we met a null node in the final level

	e.g.1
				1
			2		3
		4 5	 6
	queue = [null, null, null, null, null, null, null]
	parent =	3			4			4			5			5			6			6
	so it is complete

	e.g.2
				1
			2		3
		4 5	 		6
	queue = [null, 6, null, null, null, null]
	parent =	3		3		 4			4			5			5

	Time	O(n)
	Space	O(h)
	0 ms, faster than 100.00%
*/
func isCompleteTree1(root *TreeNode) bool {
	q := []*TreeNode{}
	q = append(q, root)
	for q[len(q)-1] != nil {
		head := q[0]
		q = q[1:]
		q = append(q, head.Left)
		q = append(q, head.Right)
	}
	for len(q) > 0 && q[len(q)-1] == nil {
		q = q[1:]
	}
	return len(q) > 0
}

func main() {

}
