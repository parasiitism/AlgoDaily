package main

import (
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st: brute force depth first search

	Time		O(n)
	Space	O(height of the tree) the call stack
	beats 14.29%
	10sep2018
*/
func closestValue(root *TreeNode, target float64) int {
	closest := root.Val
	var dfs func(cur *TreeNode)
	dfs = func(cur *TreeNode) {
		diff := math.Abs(target - float64(closest))
		cur_diff := math.Abs(target - float64(cur.Val))
		if cur_diff < diff {
			closest = cur.Val
		}
		if cur.Left != nil {
			dfs(cur.Left)
		}
		if cur.Right != nil {
			dfs(cur.Right)
		}
	}
	dfs(root)
	return closest
}

/*
	2nd: BST search
	Time		O(logn)
	Space	O(height of the tree) the call stack
	beats 100%
	20jan2019
*/
func closestValue3(root *TreeNode, target float64) int {
	closest := root.Val
	var dfs func(cur *TreeNode)
	dfs = func(cur *TreeNode) {
		diff := math.Abs(target - float64(closest))
		cur_diff := math.Abs(target - float64(cur.Val))
		if cur_diff < diff {
			closest = cur.Val
		}
		if target < float64(cur.Val) && cur.Left != nil {
			dfs(cur.Left)
		} else if target > float64(cur.Val) && cur.Right != nil {
			dfs(cur.Right)
		}
	}
	dfs(root)
	return closest
}

func main() {
}
