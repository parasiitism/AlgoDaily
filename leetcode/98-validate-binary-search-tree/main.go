package main

import (
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// intuitive way
func isValidBST(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return check(root, math.MinInt64, math.MaxInt64)
}

func check(root *TreeNode, min int, max int) bool {
	left := true
	right := true
	if root.Left != nil {
		if (root.Left.Val == math.MinInt64 || min < root.Left.Val) && root.Left.Val < root.Val {
			left = check(root.Left, min, root.Val)
		} else {
			return false
		}
	}
	if root.Right != nil {
		if root.Val < root.Right.Val && (root.Right.Val == math.MaxInt64 || root.Right.Val < max) {
			right = check(root.Right, root.Val, max)
		} else {
			return false
		}
	}
	return left && right
}

func main() {
}
