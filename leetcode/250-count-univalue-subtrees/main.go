package main

import "math"

/**
 * Definition for a binary tree node.
 */

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach: bottom up recusrion
	Time    O(n)
	Space   O(h)
	4 ms, faster than 100.00%
*/
func countUnivalSubtrees(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	var dfs func(node *TreeNode, parentVal int) int
	dfs = func(node *TreeNode, parentVal int) int {
		if node == nil {
			return parentVal
		}
		left := dfs(node.Left, node.Val)
		right := dfs(node.Right, node.Val)
		if node.Val == left && node.Val == right && left != math.MaxInt64 {
			res++
			return node.Val
		}
		return math.MaxInt64
	}
	dfs(root, math.MaxInt64)
	return res
}

func main() {

}
