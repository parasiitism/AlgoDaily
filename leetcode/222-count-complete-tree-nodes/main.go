package main

import "math"

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach dfs
	Time		O(n)
	Space		O(height of the tree)
	24ms beats 92.86%
	20jan2019
*/
func countNodes(root *TreeNode) int {
	count := 0
	var dfs func(node *TreeNode)
	dfs = func(node *TreeNode) {
		if node == nil {
			return
		}
		count++
		dfs(node.Left)
		dfs(node.Right)
	}
	dfs(root)
	return count
}

/*
	2nd approach
	- actually we dont need to go though all the nodes
	- we can just search for the node which the left and right have different height
	Time		O(h*h) worst
	Space		O(height of the tree)
	20ms beats 100%
	20jan2019
*/
func countNodes1(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left := 1 + getLeftHeight(root)
	right := 1 + getRightHeight(root)
	if left == right {
		// if left == right, it means that this subtree is a perfect tree
		// therefore the number of nodes = 2^n-1
		return int(math.Pow(2, float64(left))) - 1
	} else {
		// if unfortunately left != right, we need traverse down its children and count
		return 1 + countNodes1(root.Left) + countNodes1(root.Right)
	}
}

func getLeftHeight(root *TreeNode) int {
	if root == nil {
		return 0
	}
	height := 0
	for root.Left != nil {
		height++
		root = root.Left
	}
	return height
}

func getRightHeight(root *TreeNode) int {
	if root == nil {
		return 0
	}
	height := 0
	for root.Right != nil {
		height++
		root = root.Right
	}
	return height
}

func main() {

}
