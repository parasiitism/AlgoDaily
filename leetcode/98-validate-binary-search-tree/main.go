package main

import (
	"math"
)

/*
	Questions to ask:
	- what if there are duplicate node.vals?
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
	naive approach
	- compare the left & right to min & max before recursion
	12ms beats 30.77%
	25sep2018
*/
func isValidBST1(root *TreeNode) bool {
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

/*
	2nd approach
	- compare the node.val with min & max in each recursion
	8ms beats 100%
	14jan2019
*/
func isValidBST2(root *TreeNode) bool {
	var check func(node *TreeNode, min int, max int) bool
	check = func(node *TreeNode, min int, max int) bool {
		if node == nil {
			return true
		}
		if node.Val <= min || node.Val >= max {
			return false
		}
		return check(node.Left, min, node.Val) && check(node.Right, node.Val, max)
	}
	return check(root, math.MinInt64, math.MaxInt64)
}

/*
	3rd approach
	- compare the node.val with min & max in each iteration
	8ms beats 100%
	14jan2019
*/
type Stack struct {
	Node *TreeNode
	Min  int
	Max  int
}

func isValidBST(root *TreeNode) bool {
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
