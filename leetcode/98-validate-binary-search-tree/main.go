package main

import (
	"math"
)

/*
	Questions to ask:
	- what if there are duplicate node.vals? if there are duplicate values, it is invalid
	- what is the integraer range of node.val? -2^32 -> 2^32-1 ?

	Follow up:
	- find the invalid node in a BST
*/

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

/*
	1st approach
	- compare the node.val with min & max in each recursion
	Time 	O(n)
	Space	O(h)
	4ms beats 100%
	14jan2019
*/
func isValidBST(root *TreeNode) bool {
	return dfs(root, math.MinInt64, math.MaxInt64)
}

func dfs(node *TreeNode, min int, max int) bool {
	if node == nil {
		return true
	}
	if node.Val <= min || node.Val >= max {
		return false
	}
	return dfs(node.Left, min, node.Val) && dfs(node.Right, node.Val, max)
}

/*
	2nd approach
	- compare the node.val with min & max in each iteration
	8ms beats 100%
	14jan2019
*/
type Stack struct {
	Node *TreeNode
	Min  int
	Max  int
}

func isValidBST1(root *TreeNode) bool {
	if root == nil {
		return true
	}
	stack := []Stack{} // i dont need to check if the stack is nil, so no need to use pointer
	stack = append(stack, Stack{root, math.MinInt64, math.MaxInt64})
	for len(stack) > 0 {
		pop := stack[len(stack)-1]
		curNode := pop.Node
		stack = stack[:len(stack)-1]
		if curNode.Val <= pop.Min || curNode.Val >= pop.Max {
			return false
		}
		if curNode.Left != nil {
			stack = append(stack, Stack{curNode.Left, pop.Min, curNode.Val})
		}
		if curNode.Right != nil {
			stack = append(stack, Stack{curNode.Right, curNode.Val, pop.Max})
		}
	}
	return true
}

func main() {
}
