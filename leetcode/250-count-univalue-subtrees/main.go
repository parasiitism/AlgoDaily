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
	- return the value of the node if it is a univalue subtree

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

/*
	1st approach: bottom up recusrion
	- but return boolean instead of int value

	Time    O(n)
	Space   O(h)
	4 ms, faster than 100.00%
*/
func countUnivalSubtrees1(root *TreeNode) int {
	if root == nil {
		return 0
	}
	res := 0
	var dfs func(node *TreeNode) bool
	dfs = func(node *TreeNode) bool {
		if node == nil {
			return true
		}
		left := dfs(node.Left)
		right := dfs(node.Right)

		if left == false || right == false {
			return false
		}

		if node.Left != nil && node.Val != node.Left.Val {
			return false
		}
		if node.Right != nil && node.Val != node.Right.Val {
			return false
		}
		res++
		return true
	}
	dfs(root)
	return res
}

func main() {

}
